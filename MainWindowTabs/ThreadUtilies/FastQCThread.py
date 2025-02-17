import sys
import re
import subprocess
import os
import logging
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QProgressBar, QPushButton
from PySide6.QtCore import QThread, Signal

class FastQCThread(QThread):
    output_signal = Signal(str)
    progress_signal = Signal(int)
    finished_signal = Signal(str)

    def __init__(self, input_files, output_dir, threads=6):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.input_files = input_files
        self.output_dir = output_dir
        self.threads = threads
        self.task_counter = 0
        self.proccess_percentage = 0
        self.fastqc_path = self.find_fastqc()  # 动态查找 fastqc 路径
        self.process = None  # 保存 subprocess.Popen 对象


    def find_fastqc(self):
        # 优先检查常见路径（Windows/macOS/Linux）
        possible_paths = [
            "fastqc",  # 假设已在 PATH 中
            "/usr/local/bin/fastqc",  # macOS/Linux 常见路径
            "C:\\Program Files\\FastQC\\fastqc.exe"  # Windows 默认安装路径
        ]
        for path in possible_paths:
            if os.path.exists(path):
                self.logger.debug("fastqc path: %s", path)
                return path
        raise FileNotFoundError("FastQC not found. Please ensure it is installed and in the PATH.")

    def run(self):
        try:
            self.logger.info("Start fastQC report thread!")
            # 确保输出目录存在
            os.makedirs(self.output_dir, exist_ok=True)

            # 构造命令（避免 shell=True）
            command = [
                self.fastqc_path,
                "-t", str(self.threads),
                "-o", self.output_dir
            ] + self.input_files

            # 启动进程
            self.process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,  # 合并 stdout 和 stderr
                universal_newlines=True
            )

            # 实时捕获输出
            while True:
                output = self.process.stdout.readline()
                if output == '' and self.process.poll() is not None:
                    break
                if output:
                    self.output_signal.emit(output.strip())
                    self.update_progress_bar(output.strip())

            # 检查返回值, fastqc 进程被请求终止返回143
            if self.process.returncode != 0 and self.process.returncode != 143:
                self.output_signal.emit(f"Error: FastQC exited with code {self.process.returncode}")
            else:
                # finished FastQC analysis successfully
                self.finished_signal.emit("Successfull")  # 发送新文件列表
        except Exception as e:
            self.output_signal.emit(f"Error: {str(e)}")

    def extract_first_percentage(self, text):
        match = re.search(r"(\d+\.?\d*)%", text)
        return int(match.group(1)) if match else None
    
    def update_progress_bar(self, text):
        self.logger.info(text)
        if text is None:
            return
        
        if "Started analysis" in text:
            self.task_counter += 1
            return
        
        if "Analysis complete" in text:
            self.task_counter -= 1
            if self.task_counter == 0:
                self.progress_signal.emit(100)
            return
        
        if "Approx" in text:
            percentage = self.extract_first_percentage(text)
            if self.proccess_percentage < percentage:
                self.proccess_percentage = percentage
                self.progress_signal.emit(self.proccess_percentage)

    def stop(self):
        """
        终止 fastqc 进程
        """
        self.logger.info("Terminate FastQC process!")
        if self.process and self.process.poll() is None:  # 检查进程是否仍在运行
            self.process.terminate()  # 终止进程
            self.process.wait()  # 等待进程结束
