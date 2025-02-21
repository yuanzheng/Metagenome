import os
import config.config as config
import logging
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap
from gui.ui_generated.mainwindow_ui import Ui_MainWindow
from gui.setup import SetupWindow
from core.fastq_analysis.fastqc_report import FastQCReportProcessor


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.setupUi(self)

        self.tabWidget.setCurrentIndex(0)

        self.actionQuit.triggered.connect(self.close)
        self.actionSetup.triggered.connect(self.editSetup)

        # Initailze tab FastQC Report
        self.fastQC_tab_logic = FastQCReportProcessor(self.tab_fastqcreport)
        self.pushButton_fastQC_Report.clicked.connect(self.fastQC_tab_logic.generate_fastqc_report)
        self.fastqcRadioButtonGroup.buttonToggled.connect(self.fastQC_tab_logic.clickon_radio_button)
        self.listWidget_fastqcreport.currentRowChanged.connect(self.fastQC_tab_logic.display_image_for_fastqc_report)

    def editSetup(self):
        self.setup = SetupWindow()
        self.setup.show()

    def closeEvent(self, event):
        """
        重写关闭事件，确保关闭窗口时终止 fastqc 进程
        """
        self.logger.info("Shut down the running thread")
        for thread in config.threads:
            if thread.isRunning():
                thread.stop()  # 终止 每一个 进程
                thread.quit()  # 终止线程
                thread.wait()  # 等待线程结束
        event.accept()  # 接受关闭事件
        