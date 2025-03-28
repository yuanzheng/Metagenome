import glob
import logging
import os
import re
import zipfile
from pathlib import Path

from PySide6.QtCore import QByteArray, QSize, Qt, Slot
from PySide6.QtGui import QImage, QPainter, QPixmap
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import (
    QLabel,
    QListWidget,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QRadioButton,
)

import constant_values.config as config
from utils.thread_utilies.fastqc_thread import FastQCThread


class FastQCReportProcessor:

    def __init__(self, tab_widget):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.tab_widget = tab_widget
        self.output_dir = ""
        self.pushButton_fastQC_Report = tab_widget.findChild(
            QPushButton, "pushButton_fastQC_Report"
        )
        self.pushButton_fastQC_Report.clicked.connect(self.generate_fastqc_report)

        self.radioButton_base_seq_quality = tab_widget.findChild(
            QRadioButton, "radioButton_base_seq_quality"
        )
        self.radioButton_base_seq_content = tab_widget.findChild(
            QRadioButton, "radioButton_base_seq_content"
        )
        self.listWidget_fastqcreport = tab_widget.findChild(
            QListWidget, "listWidget_fastqcreport"
        )
        self.listWidget_fastqcreport.currentRowChanged.connect(
            self.display_image_for_fastqc_report
        )
        self.label_image = tab_widget.findChild(QLabel, "label_image")
        self.progress_bar = tab_widget.findChild(QProgressBar, "progressBar_fastqc")

    @Slot()
    def generate_fastqc_report(self):
        self.logger.debug(
            "Check global variable, fastQDataDirectory: %s", config.FASTQ_DATA_DIRECTORY
        )

        self.output_dir = (
            Path(config.FASTQ_DATA_DIRECTORY) / config.FASTQC_REPORT_DIRECTORY
        )

        directory = Path(config.FASTQ_DATA_DIRECTORY)

        # Open the output directory and load zip file names to listwidget
        # check if directory exists, and if directory is empty
        fastqc_report_list = self._list_fastqc_report(self.output_dir)
        self.logger.debug("Run FastQC script to generate reports")
        self.listWidget_fastqcreport.clear()
        self.listWidget_fastqcreport.addItems(fastqc_report_list)
        # Run FastQC script
        # 使用 glob 手动扩展文件列表（跨平台兼容）
        try:
            if directory.exists():  # Path.exists(fastq_file_directory):
                input_files = glob.glob(
                    os.path.join(config.FASTQ_DATA_DIRECTORY, "*.fastq.gz")
                )
                if not input_files:
                    self.logger.error(
                        "No .fastq.gz files found in "
                        + config.FASTQ_DATA_DIRECTORY
                        + "\n"
                    )
                    QMessageBox.critical(
                        self.tab_widget,
                        "错误",
                        "No .fastq.gz files found, 请先设置FASTQ文件所在目录路径",
                    )
                    return

                input_files = self._filter_fastqc_report(
                    input_files, fastqc_report_list
                )
            else:
                self.logger.error(
                    "Directory path "
                    + config.FASTQ_DATA_DIRECTORY
                    + " doesn't exist.\n"
                )
                QMessageBox.critical(
                    self.tab_widget,
                    "错误",
                    f"{config.FASTQ_DATA_DIRECTORY} not found, 请先设置FASTQ文件所在目录路径",
                )
                return
        except Exception as e:
            self.logger.exception(
                "An error occurred while opening the selected directory: %s\n", e
            )

        if not input_files:
            return
        self.logger.debug("Files %s for generating fastqc report", input_files)

        # 启动线程
        thread = FastQCThread(input_files, self.output_dir)
        thread.output_signal.connect(self.update_output)
        # Update progress bar
        thread.progress_signal.connect(self.progress_bar.setValue)
        # Add zip file name to self.listWidget_fastqcreport
        # Enable self.radioButton_base_seq_quality
        # Enable self.radioButton_base_seq_content
        thread.finished_signal.connect(self.show_new_files)
        thread.start()
        # 将当前线程放入线程池。在关闭app时确保所有线程被终止
        config.threads.append(thread)
        self.progress_bar.setValue(0.5)
        self.pushButton_fastQC_Report.setEnabled(False)

    @Slot()
    def clickon_radio_button(self):
        if self.radioButton_base_seq_quality.isChecked():
            self.logger.info("base_seq_quality is selected")
            self.display_image_for_fastqc_report()

        if self.radioButton_base_seq_content.isChecked():
            self.logger.info("base_seq_content is selected")
            self.display_image_for_fastqc_report()

    def selected_radio_button(self):
        if self.radioButton_base_seq_quality.isChecked():
            self.logger.info("base_seq_quality is on")
            return config.FASTQC_REPORT_IMAGE_SEQUENCE_QUALITY

        if self.radioButton_base_seq_content.isChecked():
            self.logger.info("base_seq_content is on")
            return config.FASTQC_REPORT_IMAGE_SEQUENCE_CONTENT

    @Slot()
    def display_image_for_fastqc_report(self):
        if self.listWidget_fastqcreport.currentRow() >= 0:
            fileName = self.listWidget_fastqcreport.currentItem().text()
            self.logger.debug("display image for file: %s", fileName)
            self.logger.debug("from the directory: %s", self.output_dir)
            zip_path = os.path.join(self.output_dir, fileName)
            self.logger.debug("Full path is %s", zip_path)

            imageFile = self.selected_radio_button()
            self.load_zip(zip_path, imageFile)

    @Slot(str)
    def update_output(self, text):
        self.logger.info("update_output - %s", text)
        if text is None:
            return
        # TODO popup window to give the failure reason
        if "Error" in text:
            self.logger.error("update_output - %s", text)
            return

    @Slot(str)
    def show_new_files(self, status):
        self.logger.debug("Thread is done!")
        if status == "Successfull":
            self._list_fastqc_report(self.output_dir)
        else:
            self.listWidget_fastqcreport.addItem("没有找到fastqc report!")

        self.pushButton_fastQC_Report.setEnabled(True)

    def file_filter(self, files, extensions):
        results = []
        self.logger.debug("all files in directory: %s", files)
        for file in files:
            for ext in extensions:
                if file.endswith(ext):
                    results.append(file)
        return results

    def _list_fastqc_report(self, fastqc_report_directory):
        self.logger.debug("Fastqc report directory: %s", fastqc_report_directory)
        extensions = [config.FASTQC_REPORT_EXTENSION]
        sorted_fileNames = []
        try:
            if Path.exists(fastqc_report_directory):
                sorted_fileNames = sorted(
                    self.file_filter(os.listdir(fastqc_report_directory), extensions),
                    key=self._filename_sort_key,
                )
                self.listWidget_fastqcreport.clear()
                self.logger.debug("Existing fastqc reports: %s", sorted_fileNames)
                self.listWidget_fastqcreport.addItems(sorted_fileNames)

            self.logger.debug(
                "Number of items: %s", self.listWidget_fastqcreport.count()
            )

            if self.listWidget_fastqcreport.count() > 0:
                self.radioButton_base_seq_quality.setEnabled(True)
                self.radioButton_base_seq_quality.setChecked(True)
                self.radioButton_base_seq_content.setEnabled(True)

            return sorted_fileNames
        except Exception as e:
            self.logger.exception(
                "An error occurred while opening the selected directory: %s\n", e
            )
        return sorted_fileNames

    def _filename_sort_key(self, filename):
        """提取文件名中前两个独立数字作为排序依据"""
        numbers = list(map(int, re.findall(r"\d+", filename)))

        # 处理数字不足的情况
        if len(numbers) < 2:
            # 如果没有足够数字，将缺失值设为无穷大(确保排在最后)
            return (
                (numbers[0], float("inf")) if numbers else (float("inf"), float("inf"))
            )
        return (numbers[0], numbers[1])

    def load_zip(self, zip_path, image_file_name):
        """安全加载ZIP文件"""
        try:
            # 统一路径格式处理
            normalized_path = os.path.normpath(zip_path)
            if not os.path.exists(normalized_path):
                raise FileNotFoundError(f"File does not exist: {normalized_path}")

            with zipfile.ZipFile(normalized_path, "r") as zf:
                self.processZipContents(zf, image_file_name)

        except Exception as e:
            self.logger.error(f"Failed to load the image file: {str(e)}")
            self.label_image.setText(f"Failed to load the image file: {str(e)}")

    def processZipContents(self, zip_file, image_file_name):
        """处理ZIP内容"""
        found_svg = False
        for file_info in zip_file.infolist():
            if self.is_valid_svg(file_info.filename, image_file_name):
                self.logger.debug("The valid path: %s", file_info.filename)
                self.add_svg_to_label(zip_file, file_info)
                found_svg = True
                break

        if not found_svg:
            self.logger.info(
                "Not found SVG file",
                "Please check if fastqc-report zip file "
                + "includes an Images directory with .svg files",
            )

    def _filter_fastqc_report(self, fastq_file_list, fastqc_report_list):
        copy_fastq_file_list = fastq_file_list.copy()

        for fastqc_report in fastqc_report_list:
            common_part = fastqc_report.rsplit("_", 1)[0]
            # 找到并删除匹配的文件
            for file in copy_fastq_file_list[:]:
                file_name = os.path.basename(file)
                if file_name.startswith(common_part):
                    copy_fastq_file_list.remove(file)
        return copy_fastq_file_list

    def is_valid_svg(self, filename, image_filename):
        """验证文件名有效性"""
        # 统一转小写处理路径
        lower_name = filename.lower()
        # self.logger.debug("Each path in zip: %s", lower_name)
        return (
            lower_name.endswith(image_filename)
            and lower_name.split("/")[-2] == "images"
            and not lower_name.startswith(  # 兼容Linux/Windows路径
                "__"
            )  # 排除系统隐藏文件
        )

    def add_svg_to_label(self, zip_file, file_info):
        """创建SVG显示组件"""
        with zip_file.open(file_info) as f:
            svg_data = QByteArray(f.read())

            # 创建 QLabel 显示 SVG
            w, h = self.label_image.width(), self.label_image.height()
            self.logger.debug(f"SVG width and length: {str(w)}, {str(h)}")
            pixmap = self.svg_to_pixmap(svg_data, QSize(w, h))
            self.label_image.setPixmap(pixmap)

    def svg_to_pixmap(self, svg_data, size):
        """将 SVG 数据转换为 QPixmap"""
        renderer = QSvgRenderer(svg_data)
        if not renderer.isValid():
            raise ValueError("invalid SVG data")

        # 创建 QImage 并渲染 SVG
        image = QImage(size, QImage.Format_ARGB32)
        image.fill(Qt.transparent)
        painter = QPainter(image)
        renderer.render(painter)
        painter.end()

        # 转换为 QPixmap
        return QPixmap.fromImage(image)
