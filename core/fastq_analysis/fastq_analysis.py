import os
from pathlib import Path
from collections import defaultdict
from PySide6.QtCore import Qt, Slot, QThreadPool
from PySide6.QtWidgets import (
    QListWidgetItem, QListWidget, QPushButton, 
    QProgressBar, QMessageBox, QTableWidget, QTableWidgetItem,
    QCheckBox, QHeaderView)
import logging
import config.config as config
from utils.thread_utilies.fastq_analysis_thread import AnalysisTask, AnalysisSignals
from concurrent.futures import ThreadPoolExecutor


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

    @Slot()
    def start_analysis(self):
        # 初始化表格
        self.tableWidget_fastq_analysis.clear()
        self.tableWidget_fastq_analysis.setRowCount(0)
        self.table_header = self._init_table_header()   

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
        
        pool = QThreadPool.globalInstance()
        pool.setMaxThreadCount(len(selected_items))  # 限制最大并发数
        
        # 启动分析线程
        for file_id in selected_items:
            file_path = self.raw_fastq_filenames[file_id]
            thread = AnalysisTask(file_id, file_path, config.FASTQ_PARSER_EXE_FILE)
            thread.signals.started.connect(self.on_task_start)
            thread.signals.result_ready.connect(self.on_result_ready)
            thread.signals.error_occurred.connect(self.on_task_error)
            pool.start(thread)
            # 将当前线程放入线程池。在关闭app时确保所有线程被终止
            config.threads.append(thread)

    @Slot(str, str)
    def on_task_error(self, file_id, error_msg):
        """错误处理"""
        for row in range(self.tableWidget_fastq_analysis.rowCount()):
            if self.tableWidget_fastq_analysis.item(row, 0).text() == file_id:
                for index in range(1, len(self.table_header)):
                    self.logger.error("Error, column for %s: %s", self.table_header[index], error_msg)
                    item = QTableWidgetItem(f"错误: {error_msg}")
                    item.setForeground(Qt.red)
                    self.tableWidget_fastq_analysis.setItem(row, index, item)
                break

    @Slot(str, dict)
    def on_result_ready(self, file_id, result):
        if not result:
            self.logger.error("Failed to get FASTQ analysis result for file: %s", file_id)
        """成功结果处理"""
        for row in range(self.tableWidget_fastq_analysis.rowCount()):
            if self.tableWidget_fastq_analysis.item(row, 0).text() == file_id:
                for index in range(1, len(self.table_header)):
                    text = f"{result[self.table_header[index]]:,}"
                    self.logger.debug("column for %s", text)
                    item = QTableWidgetItem(text)
                    item.setForeground(Qt.darkGreen)
                    self.tableWidget_fastq_analysis.setItem(row, index, item)
                break

    @Slot(str)
    def on_task_start(self, file_id):
        """任务开始回调"""
        for row in range(self.tableWidget_fastq_analysis.rowCount()):
            if self.tableWidget_fastq_analysis.item(row, 0).text() == file_id:
                for col in range(1, self.tableWidget_fastq_analysis.columnCount()):
                    item = self.tableWidget_fastq_analysis.item(row, col)
                    item.setText("分析中...")
                    item.setForeground(Qt.darkYellow)
                break

    @Slot(str)
    def list_fastq_files(self, fastq_file_directory):
        self.logger.debug("Fastq file directory: %s", fastq_file_directory)
        extensions = [config.FASTQ_FILE_EXTENSION]
        directory = Path(fastq_file_directory)
        
        try:
            if directory.exists(): # Path.exists(fastq_file_directory):
                fileNames = self.file_filter(os.listdir(directory), extensions)
                self.listWidget_fastq_analysis.clear()
                file_set = set()
                for fileName in fileNames:
                    file_id = self.file_name_split(fileName)
                    file_set.add(file_id)
                    self.raw_fastq_filenames[file_id].append(directory / fileName)
                self.add_items_into_listwidget(sorted(file_set))
            self.logger.debug("Number of fastq files: %s", self.listWidget_fastq_analysis.count())
            return True
        except Exception as e:
            self.logger.exception("An error occurred while opening the selected directory: %s\n", e)

        return False
    
    def file_filter(self, files, extensions):
        results = []
        self.logger.debug("All files in directory: %s", files)
        for file in files:
            for ext in extensions:
                if file.endswith(ext):
                    results.append(file)
        return results
    
    def file_name_split(self, file_name):
        key = file_name.partition("_")[0]  # 分割第一个下划线前的部分
        # 转换为普通字典（如果需要）
        # result = dict(result)
        return key
    
    def add_items_into_listwidget(self, sorted_list):
        if sorted_list is None or not sorted_list:
            return
        
        self.add_select_all_item()

        for text in sorted_list:
            item = QListWidgetItem(text)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)  # 启用复选框
            item.setCheckState(Qt.Unchecked)  # 初始状态为未选中
            self.listWidget_fastq_analysis.addItem(item)
              

    def add_select_all_item(self):
        """添加全选专用项（始终显示在第一行）"""
        item = QListWidgetItem("[全选]")
        item.setData(Qt.UserRole, "SELECT_ALL")  # 设置特殊标识
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        item.setCheckState(Qt.Unchecked)
        self.listWidget_fastq_analysis.insertItem(0, item)  # 插入到第一行  

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

        return table_header

    def _init_table_row(self, selected_items):
        """初始化表格行"""       
        self.tableWidget_fastq_analysis.setRowCount(len(selected_items)) 
        for row, item in enumerate(selected_items):
            self.logger.debug("Selected items: %s and %s", row, item)
            for col in range(len(self.table_header)):
                if col == 0:
                    # 样本ID
                    self.tableWidget_fastq_analysis.setItem(row, col, QTableWidgetItem(item))
                else:
                    # 初始状态
                    status_item = QTableWidgetItem("等待分析...")
                    status_item.setForeground(Qt.gray)
                    self.tableWidget_fastq_analysis.setItem(row, col, status_item)
