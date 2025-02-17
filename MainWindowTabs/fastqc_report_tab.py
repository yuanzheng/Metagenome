import os
import glob
import config
import logging
from pathlib import Path
from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtWidgets import QLabel, QPushButton, QRadioButton, QListWidget, QProgressBar
from MainWindowTabs.ThreadUtilies.FastQCThread import FastQCThread
from PySide6.QtGui import QPixmap


class FastQCReportTab:

    def __init__(self, tab_widget):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.tab_widget = tab_widget
        self.output_dir = ""
        self.button_generate_report = tab_widget.findChild(QPushButton, "pushButton_fastQC_Report")
        self.radioButton_base_seq_quality = tab_widget.findChild(QRadioButton, "radioButton_base_seq_quality")
        self.radioButton_base_seq_content = tab_widget.findChild(QRadioButton, "radioButton_base_seq_content")
        self.listWidget_fastqcreport = tab_widget.findChild(QListWidget, "listWidget_fastqcreport")
        self.label_image = tab_widget.findChild(QLabel, "label_image")
        self.progress_bar = tab_widget.findChild(QProgressBar, "progressBar_fastqc")
        # self.listWidget.currentRowChanged.connect(self.displayImageForFastQCReport)

    @Slot()
    def generateFastQCReport(self):
        self.logger.debug("Check global variable, fastQDataDirectory: %s", config.fastQDataDirectory)
        output_text = ""
        self.output_dir = Path(config.fastQDataDirectory) / config.fastqcReportDirectory
        
        # Open the output directory and load zip file names to listwidget
        # check if directory exists, and if directory is empty
        if not self.listFastQCReport(self.output_dir):
            self.logger.debug("Run FastQC script to generate reports")
            self.listWidget_fastqcreport.clear()
            # Run FastQC script
            # 使用 glob 手动扩展文件列表（跨平台兼容）
            input_files = glob.glob(os.path.join(config.fastQDataDirectory, "*.fastq.gz"))
            if not input_files:
                self.logger.error("No .fastq.gz files found in " + config.fastQDataDirectory + "\n")
                return
            # 启动线程
            self.thread = FastQCThread(input_files, self.output_dir)
            self.thread.output_signal.connect(self.update_output)
            # Update progress bar
            self.thread.progress_signal.connect(self.progress_bar.setValue)
            # Add zip file name to self.listWidget_fastqcreport
            # Enable self.radioButton_base_seq_quality
            # Enable self.radioButton_base_seq_content
            self.thread.finished_signal.connect(self.show_new_files)
            self.thread.start()
            # Update config.fastqcReportDirectory with the newly created directory name

    def update_output(self, text):
        self.logger.info(text)
        if text is None:
            return
        # TODO popup window to give the failure reason
        if "Error" in text:
            self.logger.error(text)
            return
        
    def show_new_files(self, status):
        self.logger.debug("Thread is done!")
        if status == "Successfull":
            self.listFastQCReport(self.output_dir)
        else:
            self.listWidget_fastqcreport.addItem("没有找到fastqc report!")

    def fileFilter(self, files, extensions):
        results = []
        self.logger.debug("all files in directory: %s", files)
        for file in files:
            for ext in extensions:
                if file.endswith(ext):
                    results.append(file)
        return results
    
    def listFastQCReport(self, fastqcReportDirectory):
        self.logger.debug("Fastqc report directory: %s", fastqcReportDirectory)
        extensions = [config.fastQCReportExtension]
        try:
            if Path.exists(fastqcReportDirectory):
                fileNames = self.fileFilter(os.listdir(fastqcReportDirectory), extensions)
                self.listWidget_fastqcreport.clear()
                for fileName in fileNames:
                    self.listWidget_fastqcreport.addItem(fileName)
            self.logger.debug("Number of items: %s", self.listWidget_fastqcreport.count())
            
            if self.listWidget_fastqcreport.count() > 0:
                self.radioButton_base_seq_quality.setEnabled(True)
                self.radioButton_base_seq_quality.setChecked(True)
                self.radioButton_base_seq_content.setEnabled(True)
                return True
            return False
        except Exception as e:
            self.logger.exception("An error occurred while opening the selected directory: %s\n", e)

        return False

    def displayImageForFastQCReport(self):
        if self.listWidget_fastqcreport.currentRow() >= 0:
            fileName = self.listWidget_fastqcreport.currentItem().text()
            self.logger.debug("display image for file: %s", fileName)