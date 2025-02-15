import os
import config
import logging
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QLabel, QPushButton, QRadioButton, QListWidget
from PySide6.QtGui import QPixmap


class FastQCReportTab:
    def __init__(self, tab_widget):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.tab_widget = tab_widget
        
        self.button_generate_report = tab_widget.findChild(QPushButton, "pushButton_fastQC_Report")
        self.radioButton_base_seq_quality = tab_widget.findChild(QRadioButton, "radioButton_base_seq_quality")
        self.radioButton_base_seq_content = tab_widget.findChild(QRadioButton, "radioButton_base_seq_content")
        self.listWidget_fastqcreport = tab_widget.findChild(QListWidget, "listWidget_fastqcreport")
        self.label_image = tab_widget.findChild(QLabel, "label_image")

        #self.pushButton_fastQC_Report.clicked.connect(self.getWorkDirectory)
        # self.listWidget.currentRowChanged.connect(self.displayImageForFastQCReport)

    def fileFilter(self, files, extensions):
        results = []
        self.logger.debug("all files in directory: %s", files)
        for file in files:
            for ext in extensions:
                if file.endswith(ext):
                    results.append(file)
        return results
    
    def getWorkDirectory(self):
        self.logger.debug("Check global variable, fastqcReportDirectory: %s", config.fastqcReportDirectory)
        self.logger.debug("Check global variable, fastQDataDirectory: %s", config.fastQDataDirectory)
        self.logger.debug("Check global variable, fastQParserExefile: %s", config.fastQParserExefile)
        extensions = ['.html']
        try:
            if config.fastqcReportDirectory != "":
                fileNames = self.fileFilter(os.listdir(config.fastqcReportDirectory), extensions)
                self.listWidget_fastqcreport.clear()
                for fileName in fileNames:
                    self.listWidget_fastqcreport.addItem(fileName)
            self.logger.debug("Number of items: %s", self.listWidget_fastqcreport.count())
            
            if self.listWidget_fastqcreport.count() > 0:
                self.radioButton_base_seq_quality.setEnabled(True)
                self.radioButton_base_seq_quality.setChecked(True)
                self.radioButton_base_seq_content.setEnabled(True)
        except Exception as e:
            self.logger.exception("An error occurred while selecting a directory: %s", e)

    def displayImageForFastQCReport(self):
        if self.listWidget_fastqcreport.currentRow() >= 0:
            fileName = self.listWidget_fastqcreport.currentItem().text()
            self.logger.debug("display image for file: %s", fileName)