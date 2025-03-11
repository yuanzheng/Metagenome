import sys
import config.config as config
import logging
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QApplication, QFileDialog

from gui.ui_generated.setup_window_ui import Ui_SetupForm

class SetupWindow(QWidget, Ui_SetupForm):
    save_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)

        self.lineEdit_fastQDataDirectory.setText(config.FASTQ_DATA_DIRECTORY)
        self.lineEdit_fastQCReportDirectory.setText(config.FASTQC_REPORT_DIRECTORY)
        self.lineEdit_fastQParser.setText(config.FASTQ_PARSER_EXE_FILE)
        self.lineEdit_fastqQualityStats.setText(config.FASTQ_QUALITY_STATS_JAR_FILE)
        self.lineEdit_trimmed_fastq_directory.setText(config.FASTQ_TRIMMED_OUTPUT_DIRECTORY)

        self.pushButton_save.clicked.connect(self.saveSetupWindow)
        self.pushButton_cancel.clicked.connect(self.cancelSetupWindow)

        self.pushButton_searchFastQDataDirectory.clicked.connect(self.getFastQDataDirectory)
        self.pushButton_fastQCDirectory.clicked.connect(self.getFastQCReportDirectory)
        self.pushButton_fastQParser.clicked.connect(self.getFastQParser)
        self.pushButton_fastqQualityStats.clicked.connect(self.getFastQTrimJar)
        self.pushButton_search_trimmed_files.clicked.connect(self.getFastQTrimmedOutputDirectory)
       
    def saveSetupWindow(self):
        self.logger.info("Save the setup window")
        global fastQDataDirectory 
        config.FASTQ_DATA_DIRECTORY = self.lineEdit_fastQDataDirectory.text()

        global fastqcReportDirectory 
        config.FASTQC_REPORT_DIRECTORY = self.lineEdit_fastQCReportDirectory.text()

        global fastQParserExefile
        config.FASTQ_PARSER_EXE_FILE = self.lineEdit_fastQParser.text()

        self.save_signal.emit(config.FASTQ_DATA_DIRECTORY)
        self.logger.debug("Setup, fastQ Data Directory: %s\n" +
                          "                             fastqc Report Directory: %s\n" +
                          "                             fastQ Parser ExE file: %s\n" +
                          "                             fastQ Trimmomatic jar file: %s\n" +
                          "                             fastQ Trimmed output directory: %s\n",
                          config.FASTQ_DATA_DIRECTORY, 
                          config.FASTQC_REPORT_DIRECTORY,
                          config.FASTQ_PARSER_EXE_FILE,
                          config.FASTQ_QUALITY_STATS_JAR_FILE,
                          config.FASTQ_TRIMMED_OUTPUT_DIRECTORY
        )
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
    
    def getFastQTrimJar(self):
        fastQTrimJarFile, _ = QFileDialog.getOpenFileName(self, "select a file")
        self.lineEdit_fastqQualityStats.setText(fastQTrimJarFile)

    def getFastQTrimmedOutputDirectory(self):
        fastqTrimmedOutputDirectory = self.selectDirectory()
        self.lineEdit_trimmed_fastq_directory.setText(fastqTrimmedOutputDirectory)
    


 