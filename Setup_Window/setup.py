import sys
import config
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QWidget, QApplication, QFileDialog

from Setup_Window.UI.setup_window_ui import Ui_SetupForm

class SetupWindow(QWidget, Ui_SetupForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)

        self.lineEdit_fastQDataDirectory.setText(config.fastQDataDirectory)
        self.lineEdit_fastQCReportDirectory.setText(config.fastqcReportDirectory)
        self.lineEdit_fastQParser.setText(config.fastQParserExefile)

        self.pushButton_save.clicked.connect(self.saveSetupWindow)
        self.pushButton_cancel.clicked.connect(self.cancelSetupWindow)

        self.pushButton_searchFastQDataDirectory.clicked.connect(self.getFastQDataDirectory)
        self.pushButton_fastQCDirectory.clicked.connect(self.getFastQCReportDirectory)
        self.pushButton_fastQParser.clicked.connect(self.getFastQParser)
       
    def saveSetupWindow(self):
        print("Save it")
        global fastQDataDirectory 
        config.fastQDataDirectory = self.lineEdit_fastQDataDirectory.text()

        global fastqcReportDirectory 
        config.fastqcReportDirectory = self.lineEdit_fastQCReportDirectory.text()

        global fastQParserExefile
        config.fastQParserExefile = self.lineEdit_fastQParser.text()
        self.close()

    def cancelSetupWindow(self):
        '''
        global fastQDataDirectory 
        config.fastQDataDirectory = ""
        self.lineEdit_fastQDataDirectory.clear()
    

        global fastqcReportDirectory 
        config.fastqcReportDirectory = ""
        self.lineEdit_fastQCReportDirectory.clear()

        global fastQParserExefile
        config.fastQParserExefile = ""
        self.lineEdit_fastQParser.clear()
        '''
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


 