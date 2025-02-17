import os
import config
import logging
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap
from UI.mainwindow_ui import Ui_MainWindow
from Setup_Window.setup import SetupWindow
from MainWindowTabs.fastqc_report_tab import FastQCReportTab


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.setupUi(self)

        self.tabWidget.setCurrentIndex(0)

        self.actionQuit.triggered.connect(self.close)
        self.actionSetup.triggered.connect(self.editSetup)

        # Initailze tab FastQC Report
        self.fastQC_tab_logic = FastQCReportTab(self.tab_fastqcreport)
        self.pushButton_fastQC_Report.clicked.connect(self.fastQC_tab_logic.generateFastQCReport)
        # self.pushButton_fastQC_Report.clicked.connect(self.getWorkDirectory)
        # self.listWidget.currentRowChanged.connect(self.displayImageForFastQCReport)

    def editSetup(self):
        self.setup = SetupWindow()
        self.setup.show()

    '''
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
                self.listWidget.clear()
                for fileName in fileNames:
                    self.listWidget.addItem(fileName)
            self.logger.debug("Number of items: %s", self.listWidget.count())
            
            if self.listWidget.count() > 0:
                self.radioButton_base_seq_quality.setEnabled(True)
                self.radioButton_base_seq_quality.setChecked(True)
                self.radioButton_base_seq_content.setEnabled(True)
        except Exception as e:
            self.logger.exception("An error occurred while selecting a directory: %s", e)

    def displayImageForFastQCReport(self):
        if self.listWidget.currentRow() >= 0:
            fileName = self.listWidget.currentItem().text()
            self.logger.debug("display image for file: %s", fileName)

    '''



