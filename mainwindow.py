import os
import config
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap

from UI.mainwindow_ui import Ui_MainWindow
from Setup_Window.setup import SetupWindow

global fastqcReportDirectory

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.tabWidget.setCurrentIndex(0)

        self.actionQuit.triggered.connect(self.close)
        self.actionSetup.triggered.connect(self.editSetup)
        self.pushButton_fastQC_Report.clicked.connect(self.getWorkDirectory)

    def editSetup(self):
        self.setup = SetupWindow()
        self.setup.show()

    def getWorkDirectory(self):
        print("Check global variables, fastqcReportDirectory: ", config.fastqcReportDirectory)
        print("Check global variables, fastQDataDirectory: ", config.fastQDataDirectory)
        print("Check global variables, fastQParserExefile: ", config.fastQParserExefile)
        tmp_fastqcReportDirectory = QFileDialog.getExistingDirectory(self, "Select a directory", "~/Downloads/Bioinformatic/rawFastQc")
        extensions = ['.html']
        if tmp_fastqcReportDirectory:
            fileNames = self.fileFilter(os.listdir(tmp_fastqcReportDirectory), extensions)
            self.listWidget.clear()
            for fileName in fileNames:
                self.listWidget.addItem(fileName)

    def fileFilter(self, files, extensions):
        results = []
        print("all files in directory: ", files)
        for file in files:
            for ext in extensions:
                if file.endswith(ext):
                    results.append(file)
        return results


