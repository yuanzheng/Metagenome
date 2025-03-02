import os
from pathlib import Path
from collections import defaultdict
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (
    QListWidgetItem, QListWidget, QPushButton, 
    QProgressBar, QMessageBox, QTableWidget, QTableWidgetItem,
    QCheckBox, QHeaderView)
import logging
import config.config as config
from utils.thread_utilies.fastq_analysis_thread import AnalysisTask
from utils.thread_utilies.thread_pool import ThreadPoolManager
from utils.thread_utilies.signals import TaskType
from utils.thread_utilies.signals import signals
from core.fastq_analysis.csv_handler import CSVHandler


class FastQAnalysisProcessor:

    def __init__(self, tab_widget):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.tab_widget = tab_widget
        self.raw_fastq_filenames = defaultdict(list)
        self.bulk_update = False  # 防止批量更新时触发事件
        self.table_header = []
        self.listWidget_fastq_analysis = tab_widget.findChild(QListWidget, "listWidget_fastq_analysis")
        self.listWidget_fastq_analysis.itemChanged.connect(self.on_item_changed)  # 连接状态变化事件
        self.button_analysis_start = tab_widget.findChild(QPushButton, "button_analysis_start")
        self.button_analysis_start.clicked.connect(self.start_analysis)
        self.checkBox_total_bases = tab_widget.findChild(QCheckBox, "checkBox_total_bases")
        self.checkBox_total_reads = tab_widget.findChild(QCheckBox, "checkBox_total_reads")
        self.tableWidget_fastq_analysis = tab_widget.findChild(QTableWidget, "tableWidget_fastq_analysis")

        self.thread_pool = ThreadPoolManager()
        self.csv_handler = None
        signals.started.connect(self.on_task_start)
        signals.result_ready.connect(self.on_result_ready)
        signals.error_occurred.connect(self.on_task_error)

    @Slot()
    def start_analysis(self):
        # 初始化表格
        self.tableWidget_fastq_analysis.clear()
        self.tableWidget_fastq_analysis.setRowCount(0)
        self.table_header = self._init_table_header()

        csv_dir = Path(config.FASTQ_DATA_DIRECTORY) / config.FASTQ_ANALYSIS_REPORT_DIRECTORY
        self.csv_handler = CSVHandler(csv_dir, "stats.csv")

        """启动分析流程"""
        # 检查程序路径
        self.logger.debug("Start analysis: exe path: %s", config.FASTQ_PARSER_EXE_FILE)
        if not os.path.exists(config.FASTQ_PARSER_EXE_FILE):
            QMessageBox.critical(self.tab_widget, "错误", "请先设置分析程序路径")
            return
            
        # 获取选中文件
        selected_items = self._get_selected_items()
        if not selected_items:
            QMessageBox.warning(self.tab_widget, "警告", "请先选择要分析的文件")
            return
        
        if len(self.table_header) == 1:
            QMessageBox.warning(self.tab_widget, "警告", "选择统计项不能为空")
            return
        
        self._init_table_row(selected_items)

        # 启动分析线程
        for file_id in selected_items:
            # 避免重复统计，在缓存文件中找到已有数据直接显示在table中
            if self._statistics_exist(file_id):
                continue
        
            file_path = self.raw_fastq_filenames[file_id]
            thread = AnalysisTask(
                file_id, file_path,
                config.FASTQ_PARSER_EXE_FILE,
                task_type=TaskType.FASTQ_STATS
            )
            
            # 将当前线程放入线程池。在关闭app时确保所有线程被终止
            self.thread_pool.submit_task(task_id=file_id, task=thread)
        

    @Slot(str, TaskType, str)
    def on_task_error(self, file_id, task_type, error_msg):
        """检查线程发出的signal是否是当前类提交的任务, 如果不是直接退出"""
        if task_type != TaskType.FASTQ_STATS:
            return
        
        """错误处理"""
        for row in range(self.tableWidget_fastq_analysis.rowCount()):
            if self.tableWidget_fastq_analysis.item(row, 0).text() == file_id:
                for index in range(1, len(self.table_header)):
                    self.logger.error("Error, column for %s: %s", self.table_header[index], error_msg)
                    item = QTableWidgetItem(f"错误: {error_msg}")
                    item.setForeground(Qt.red)
                    self.tableWidget_fastq_analysis.setItem(row, index, item)
                break
        
        if self.thread_pool.alive_thread_counter() == 0:
            self.button_analysis_start.setEnabled(True)


    @Slot(str, TaskType, dict)
    def on_result_ready(self, file_id, task_type, result):
        """检查线程发出的signal是否是当前类提交的任务，如果不是直接退出"""
        if task_type != TaskType.FASTQ_STATS:
            return
        
        if not result:
            self.logger.error("Failed to get FASTQ analysis result for file: %s", file_id)
            return
        
        self.logger.debug("Print result for file %s with result: %s", file_id, result)
        """成功结果处理"""
        for row in range(self.tableWidget_fastq_analysis.rowCount()):
            self.logger.debug("table widget row: %s", row)
            if self.tableWidget_fastq_analysis.item(row, 0).text() == file_id:
                for index in range(1, len(self.table_header)):
                    text = f"{result[self.table_header[index]]:,}"
                    self.logger.debug("column for %s", text)
                    item = QTableWidgetItem(text)
                    item.setForeground(Qt.darkGreen)
                    self.tableWidget_fastq_analysis.setItem(row, index, item)
                break
        if self.thread_pool.alive_thread_counter() == 0:
            self.button_analysis_start.setEnabled(True)

        """缓存已算出的数据到本地硬盘文件中"""
        if self.csv_handler is not None:
            self.csv_handler.append_result(file_id, self.table_header, result)

    @Slot(str, TaskType) 
    def on_task_start(self, file_id, task_type):
        """检查线程发出的signal是否是当前类提交的任务，如果不是直接退出"""
        if task_type != TaskType.FASTQ_STATS:
            return
        
        for row in range(self.tableWidget_fastq_analysis.rowCount()):
            if self.tableWidget_fastq_analysis.item(row, 0).text() == file_id:
                for col in range(1, self.tableWidget_fastq_analysis.columnCount()):
                    item = self.tableWidget_fastq_analysis.item(row, col)
                    item.setText("分析中...")
                    item.setForeground(Qt.darkYellow)
                break
        self.button_analysis_start.setEnabled(False)

    @Slot(str)
    def list_fastq_files(self, fastq_file_directory):
        self.logger.debug("Fastq file directory: %s", fastq_file_directory)
        extensions = [config.FASTQ_FILE_EXTENSION]
        directory = Path(fastq_file_directory)
        
        try:
            if directory.exists(): # Path.exists(fastq_file_directory):
                fileNames = self._file_filter(os.listdir(directory), extensions)
                self.listWidget_fastq_analysis.clear()
                file_set = set()
                for fileName in fileNames:
                    file_id = self._file_name_split(fileName)
                    file_set.add(file_id)
                    self.raw_fastq_filenames[file_id].append(directory / fileName)
                self._add_items_into_listwidget(sorted(file_set))
            self.logger.debug("Number of fastq files: %s", self.listWidget_fastq_analysis.count())
            return True
        except Exception as e:
            self.logger.exception("An error occurred while opening the selected directory: %s\n", e)

        return False
    
    def _file_filter(self, files, extensions):
        results = []
        self.logger.debug("All files in directory: %s", files)
        for file in files:
            for ext in extensions:
                if file.endswith(ext):
                    results.append(file)
        return results
    
    def _file_name_split(self, file_name):
        key = file_name.partition("_")[0]  # 分割第一个下划线前的部分
        return key
    
    def _add_items_into_listwidget(self, sorted_list):
        if sorted_list is None or not sorted_list:
            return
        
        self._add_select_all_item()

        for text in sorted_list:
            item = QListWidgetItem(text)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)  # 启用复选框
            item.setCheckState(Qt.Unchecked)  # 初始状态为未选中
            self.listWidget_fastq_analysis.addItem(item)
              

    def _add_select_all_item(self):
        """添加全选专用项（始终显示在第一行）"""
        item = QListWidgetItem("[全选]")
        item.setData(Qt.UserRole, "SELECT_ALL")  # 设置特殊标识
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        item.setCheckState(Qt.Unchecked)
        self.listWidget_fastq_analysis.insertItem(0, item)  # 插入到第一行  

    @Slot()
    def on_item_changed(self, item):
        """处理选项状态变化"""
        if self.bulk_update:
            return

        # 判断是否全选项
        if item.data(Qt.UserRole) == "SELECT_ALL":
            self.bulk_update = True
            state = item.checkState()
            
            # 更新所有普通项状态
            for i in range(1, self.listWidget_fastq_analysis.count()):
                self.listWidget_fastq_analysis.item(i).setCheckState(state)
            
            self.bulk_update = False
        else:
            # 检查是否需要更新全选项状态
            all_checked = True
            for i in range(1, self.listWidget_fastq_analysis.count()):
                if self.listWidget_fastq_analysis.item(i).checkState() != Qt.Checked:
                    all_checked = False
                    break
            
            self.bulk_update = True
            self.listWidget_fastq_analysis.item(0).setCheckState(
                Qt.Checked if all_checked else Qt.Unchecked
            )
            self.bulk_update = False

    def _get_selected_items(self):
        num_items = self.listWidget_fastq_analysis.count()
        selected_items = []
        if num_items == 0:
            return selected_items
        
        for index in range(1, num_items):
            state = self.listWidget_fastq_analysis.item(index).checkState()
            if state == Qt.Checked:
                self.logger.debug("--- Selected items %s", self.listWidget_fastq_analysis.item(index).text())
                selected_items.append(self.listWidget_fastq_analysis.item(index).text())
        return selected_items

    def _init_table_header(self):
        table_header = [config.FASTQ_TOTAL_SAMPLEID]
        if self.checkBox_total_reads.isChecked():
            table_header.append(config.FASTQ_TOTAL_READS)
        if self.checkBox_total_bases.isChecked():
            table_header.append(config.FASTQ_TOTAL_BASES)
        # 准备表格
        self.tableWidget_fastq_analysis.setColumnCount(len(table_header))
        self.tableWidget_fastq_analysis.setHorizontalHeaderLabels(table_header)
        self.tableWidget_fastq_analysis.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_fastq_analysis.setSortingEnabled(True)
        return table_header

    def _init_table_row(self, selected_items):
        """初始化表格行"""       
        self.tableWidget_fastq_analysis.setRowCount(len(selected_items)) 
        for row, item in enumerate(selected_items):
            self.logger.debug("Initialize table for the selected items: %s and %s", row, item)
            for col in range(len(self.table_header)):
                if col == 0:
                    # 样本ID
                    self.tableWidget_fastq_analysis.setItem(row, col, QTableWidgetItem(item))
                else:
                    # 初始状态
                    status_item = QTableWidgetItem("等待分析...")
                    status_item.setForeground(Qt.gray)
                    self.tableWidget_fastq_analysis.setItem(row, col, status_item)

    def _task_skipped(self, existing):
        if existing is None:
            return
        
        """成功结果处理"""
        for row in range(self.tableWidget_fastq_analysis.rowCount()):
            self.logger.debug("Task skipped because exists %s", existing)
            self.logger.debug("Table widget in row %s for file: %s", row, self.tableWidget_fastq_analysis.item(row, 0).text())
            if existing[self.table_header[0]] == self.tableWidget_fastq_analysis.item(row, 0).text():
                for index in range(1, len(self.table_header)):
                    text = f"{int(existing[self.table_header[index]]):,}"
                    self.logger.debug("column for %s", text)
                    item = QTableWidgetItem(text)
                    item.setForeground(Qt.darkGreen)
                    self.tableWidget_fastq_analysis.setItem(row, index, item)
                break

    def _statistics_exist(self, file_id):
        if self.csv_handler.has_file_id(file_id):
            existing_one = self.csv_handler.get_existing_data(file_id)
            self._task_skipped(existing_one)
            return True
        
        return False
                
        
