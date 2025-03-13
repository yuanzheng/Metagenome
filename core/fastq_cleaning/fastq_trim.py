import os
from pathlib import Path
from collections import defaultdict
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (
    QListWidgetItem, QListWidget, QPushButton, 
    QProgressBar, QComboBox, QSpinBox, QMessageBox, QTableWidget, QTableWidgetItem,
    QCheckBox, QHeaderView)
import logging
import config.config as config
from utils.thread_utilies.fastq_analysis_thread import AnalysisTask
from utils.thread_utilies.thread_pool import ThreadPoolManager
from utils.thread_utilies.signals import TaskType
from utils.thread_utilies.signals import signals
from core.fastq_analysis.csv_handler import CSVHandler


class FastQTrimProcessor:

    def __init__(self, tab_widget):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.tab_widget = tab_widget
        self._raw_fastq_filenames = defaultdict(list)
        self._bulk_update = False  # 防止批量更新时触发事件
        self._table_header = []
        self.listWidget_trim_rawdata = tab_widget.findChild(QListWidget, "listWidget_trim_rawdata")
        self.listWidget_trim_rawdata.itemChanged.connect(self.on_item_changed)  # 连接状态变化事件

        self.progressBar_trim_tab = tab_widget.findChild(QProgressBar, "progressBar_trim_tab")
        self._progress_counter = 0  # 在progress bar上显示当前进度%比

        self.comboBox_trim_paired_end = tab_widget.findChild(QComboBox, "comboBox_trim_paired_end")
        self.comboBox_trim_paired_end.addItems(config.FASTQ_TRIM_OPTIONS)
        self.comboBox_trim_paired_end.currentTextChanged.connect(self._option_text_changed)
        self._trim_option = ""

        self.spinBox_trim_window_size = tab_widget.findChild(QSpinBox, "spinBox_trim_window_size")
        self.spinBox_trim_window_size.valueChanged.connect(self.update_param_values)
        
        self.listWidget_trim_params_orders = tab_widget.findChild(QListWidget, "listWidget_trim_params_orders")
        self.listWidget_trim_params_orders.model().rowsMoved.connect(self.update_param_order)

    def _init_order_parameter(self):
        """根据列表项显示/隐藏对应控件"""
        for i in range(self.listWidget_trim_params_orders.count()):
            item = self.listWidget_trim_params_orders.item(i)
            self.toggle_param_visibility(item.text(), True)

    def toggle_param_visibility(self, param_name, show):
        """控制参数控件的可见性"""
        widget_info = self.param_widgets.get(param_name)
        if widget_info:
            for widget_name in widget_info:
                if widget_name:
                    getattr(self, widget_name).parent().setVisible(show)

    def update_param_order(self):
        """当拖拽发生时更新参数显示顺序"""
        current_items = [self.listWidget_trim_params_orders.item(i).text() 
                        for i in range(self.listWidget_trim_params_orders.count())]
        
        # 隐藏所有参数控件
        for param in self.param_widgets:
            self.toggle_param_visibility(param, False)
        
        # 按新顺序显示控件
        for param in current_items:
            self.toggle_param_visibility(param, True)

    def save_parameter_order(self):
        return [self.listWidget_trim_params_orders.item(i).text() 
            for i in range(self.listWidget_trim_params_orders.count())]

    def load_parameter_order(self, order_list):
        self.listWidget_trim_params_orders.clear()
        self.listWidget_trim_params_orders.addItems(order_list)

    def build_command(self, sample):
        cmd = [...]  # 基础命令
        
        # 按当前顺序添加参数
        param_order = self.save_parameter_order()
        for param in param_order:
            if param == "LEADING":
                cmd.append(f"LEADING:{self.spin_leading.value()}")
            elif param == "SLIDINGWINDOW":
                cmd.append(f"SLIDINGWINDOW:{self.spin_window_size.value()}:{self.spin_quality.value()}")
            # 其他参数处理...
        
        return cmd

    @Slot(str)
    def _option_text_changed(self, item):
        self._trim_option = item
        self.logger.debug("PE / SE changed to %s", item)

    @Slot()
    def on_item_changed(self, item):
        """处理选项状态变化"""
        if self._bulk_update:
            return

        # 判断是否全选项
        if item.data(Qt.UserRole) == "SELECT_ALL":
            self._bulk_update = True
            state = item.checkState()
            
            # 更新所有普通项状态
            for i in range(1, self.listWidget_trim_rawdata.count()):
                self.listWidget_trim_rawdata.item(i).setCheckState(state)
            
            self._bulk_update = False
        else:
            # 检查是否需要更新全选项状态
            all_checked = True
            for i in range(1, self.listWidget_trim_rawdata.count()):
                if self.listWidget_trim_rawdata.item(i).checkState() != Qt.Checked:
                    all_checked = False
                    break
            
            self._bulk_update = True
            self.listWidget_trim_rawdata.item(0).setCheckState(
                Qt.Checked if all_checked else Qt.Unchecked
            )
            self._bulk_update = False

    @Slot(str)
    def list_fastq_files(self, fastq_file_directory):
        self.logger.debug("Fastq file directory: %s", fastq_file_directory)
        extensions = [config.FASTQ_FILE_EXTENSION]
        directory = Path(fastq_file_directory)
        self._init_progress_bar()

        try:
            if directory.exists(): # Path.exists(fastq_file_directory):
                fileNames = self._file_filter(os.listdir(directory), extensions)
                self.listWidget_trim_rawdata.clear()
                file_set = set()
                for fileName in fileNames:
                    file_id = self._file_name_split(fileName)
                    file_set.add(file_id)
                    self._raw_fastq_filenames[file_id].append(directory / fileName)
                self._add_items_into_listwidget(sorted(file_set))
            self.logger.debug("Number of fastq files: %s", self.listWidget_trim_rawdata.count())
            return True
        except Exception as e:
            self.logger.exception("An error occurred while opening the selected directory: %s\n", e)

        return False
    
    def _init_progress_bar(self):
        self._progress_counter = 0  # update progress bar to 0%
        self._update_progress(self._progress_counter)
        self._thread_progress = 0

    def _update_progress(self, increase_value):
        self._progress_counter += increase_value
        self.progressBar_trim_tab.setValue(self._progress_counter)

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
            self.listWidget_trim_rawdata.addItem(item)

    def _add_select_all_item(self):
        """添加全选专用项（始终显示在第一行）"""
        item = QListWidgetItem("[全选]")
        item.setData(Qt.UserRole, "SELECT_ALL")  # 设置特殊标识
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        item.setCheckState(Qt.Unchecked)
        self.listWidget_trim_rawdata.insertItem(0, item)  # 插入到第一行  