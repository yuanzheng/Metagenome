import sys
import config
import logging
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QWidget, QApplication, QFileDialog

from setup_window.ui_package.setup_window_ui import Ui_SetupForm

class SetupWindow(QWidget, Ui_SetupForm):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)

        self.lineEdit_fastQDataDirectory.setText(config.FASTQ_DATA_DIRECTORY)
        self.lineEdit_fastQCReportDirectory.setText(config.FASTQC_REPORT_DIRECTORY)
        self.lineEdit_fastQParser.setText(config.FASTQ_PARSER_EXE_FILE)

        self.pushButton_save.clicked.connect(self.saveSetupWindow)
        self.pushButton_cancel.clicked.connect(self.cancelSetupWindow)

        self.pushButton_searchFastQDataDirectory.clicked.connect(self.getFastQDataDirectory)
        self.pushButton_fastQCDirectory.clicked.connect(self.getFastQCReportDirectory)
        self.pushButton_fastQParser.clicked.connect(self.getFastQParser)
       
    def saveSetupWindow(self):
        self.logger.info("Save the setup window")
        global fastQDataDirectory 
        config.FASTQ_DATA_DIRECTORY = self.lineEdit_fastQDataDirectory.text()

        global fastqcReportDirectory 
        config.FASTQC_REPORT_DIRECTORY = self.lineEdit_fastQCReportDirectory.text()

        global fastQParserExefile
        config.FASTQ_PARSER_EXE_FILE = self.lineEdit_fastQParser.text()
        self.logger.debug("Setup, fastQ Data Directory: %s\n" +
                          "fastqc Report Directory: %s\nand " +
                          "fastQ Parser ExE file: %s", 
                          config.FASTQ_DATA_DIRECTORY, 
                          config.FASTQC_REPORT_DIRECTORY,
                          config.FASTQ_PARSER_EXE_FILE)
        self.close()

    def cancelSetupWindow(self):
        self.close()


    def getFastQDataDirectory(self):
        fastQDataDirectory = self.selectDirectory()
        self.lineEdit_fastQDataDirectory.setText(fastQDataDirectory)


    def getFastQCReportDirectory(self):
        fastqcReportDirectory = self.selectDirectory()
        self.lineEdit_fastQCReportDirectory.setText(fastqcReportDirectory)

    def getFastQParser(self):
        fastQParserExeFile, _ = QFileDialog.getOpenFileName(self, "select a file")
        self.lineEdit_fastQParser.setText(fastQParserExeFile)

    def selectDirectory(self):
        return QFileDialog.getExistingDirectory(self, "Select a directory")


 