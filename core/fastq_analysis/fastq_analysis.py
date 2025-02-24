import os
from pathlib import Path
from collections import defaultdict
from PySide6.QtCore import Qt, Slot, QByteArray, QSize
from PySide6.QtWidgets import QListWidgetItem, QListWidget, QProgressBar
import logging
import config.config as config


class FastQAnalysisProcessor:

    def __init__(self, tab_widget):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.tab_widget = tab_widget
        self.raw_fastq_filenames = defaultdict(list)

        self.listWidget_fastq_analysis = tab_widget.findChild(QListWidget, "listWidget_fastq_analysis")



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
                self.add_items_into_listwidget(sorted(file_set))
            self.logger.debug("Number of fastq files: %s", self.listWidget_fastq_analysis.count())
            return True
        except Exception as e:
            self.logger.exception("An error occurred while opening the selected directory: %s\n", e)

        return False
    
    def file_filter(self, files, extensions):
        results = []
        self.logger.debug("all files in directory: %s", files)
        for file in files:
            for ext in extensions:
                if file.endswith(ext):
                    results.append(file)
        return results
    
    def file_name_split(self, file_name):
        key = file_name.partition("_")[0]  # 分割第一个下划线前的部分
        self.raw_fastq_filenames[key].append(file_name)

        # 转换为普通字典（如果需要）
        # result = dict(result)
        return key
    
    def add_items_into_listwidget(self, sorted_list):
        for text in sorted_list:
            item = QListWidgetItem(text)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)  # 启用复选框
            item.setCheckState(Qt.Unchecked)  # 初始状态为未选中
            self.listWidget_fastq_analysis.addItem(item)        
