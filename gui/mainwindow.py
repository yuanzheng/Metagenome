import config.config as config
import logging
from PySide6.QtWidgets import QMainWindow
from gui.ui_generated.mainwindow_ui import Ui_MainWindow
from gui.setup import SetupWindow
from core.fastq_analysis.fastq_analysis import FastQAnalysisProcessor
from core.fastq_analysis.fastqc_report import FastQCReportProcessor
from utils.thread_utilies.thread_pool import app_state
from utils.thread_utilies.thread_pool import ThreadPoolManager


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.setupUi(self)
        self.thread_pool = ThreadPoolManager()
        self.tabWidget.setCurrentIndex(0)

        self.actionQuit.triggered.connect(self.close)
        self.actionSetup.triggered.connect(self.editSetup)

        # Initialize tab FastQ Analysis
        self.fastQ_analysis_tab_logic = FastQAnalysisProcessor(self.tab_rawdata)

        # Initialize tab FastQC Report
        self.fastQC_tab_logic = FastQCReportProcessor(self.tab_fastqcreport)
        self.fastqcRadioButtonGroup.buttonToggled.connect(self.fastQC_tab_logic.clickon_radio_button)

        
    def editSetup(self):
        self.setup = SetupWindow()
        self.setup.show()
        self.setup.save_signal.connect(self.fastQ_analysis_tab_logic.list_fastq_files)

    def closeEvent(self, event):
         # 设置全局退出标志
        app_state.request_exit()
        self.thread_pool.stop_all()
        
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
        super().closeEvent(event)




        