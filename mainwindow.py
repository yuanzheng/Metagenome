import os
import config
import logging
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap
from UI.mainwindow_ui import Ui_MainWindow
from Setup_Window.setup import SetupWindow

global fastqcReportDirectory

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.setupUi(self)
        self.app = app
        self.tabWidget.setCurrentIndex(0)

        self.actionQuit.triggered.connect(self.close)
        self.actionSetup.triggered.connect(self.editSetup)
        self.pushButton_fastQC_Report.clicked.connect(self.getWorkDirectory)

    def editSetup(self):
        self.setup = SetupWindow()
        self.setup.show()

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
        tmp_fastqcReportDirectory = QFileDialog.getExistingDirectory(self, "Select a directory", "~/Downloads/Bioinformatic/rawFastQc")
        extensions = ['.html']
        try:
            if tmp_fastqcReportDirectory:
                fileNames = self.fileFilter(os.listdir(tmp_fastqcReportDirectory), extensions)
                self.listWidget.clear()
                for fileName in fileNames:
                    self.listWidget.addItem(fileName)
        except Exception as e:
            self.logger.exception("An error occurred while selecting a directory: %s", e)


