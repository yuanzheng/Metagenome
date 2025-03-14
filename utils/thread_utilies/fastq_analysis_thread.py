import logging
import os
import re
import signal
import subprocess  # nosec

from PySide6.QtCore import QRunnable

import constant_values.config as config
from utils.thread_utilies.signals import signals
from utils.thread_utilies.thread_pool import app_state


# ==============================
# 可执行分析任务线程
# ==============================
class AnalysisTask(QRunnable):

    def __init__(self, file_id, file_path, program_path, task_type):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.file_id = file_id
        self.file_path = file_path
        self.program_path = program_path
        self.task_type = task_type
        self.process = None  # 保存进程句柄
        self.setAutoDelete(True)  # 任务完成后自动清理

    def run(self):
        if app_state.check_exit():
            self.logger.debug("Quit this thread to give up analysis %s ", self.file_id)
            return
        signals.started.emit(self.file_id, self.task_type)

        try:
            self.logger.info("Start fastQ analysis thread for %s", self.file_id)

            # 构造跨平台命令
            cmd = self._build_command()

            # 执行外部程序
            self.process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                shell=False,
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0,
            )  # nosec

            # 实时监控退出请求
            while self.process.poll() is None:
                if app_state.check_exit():
                    self.logger.debug(
                        "Requested to terminate the thread,  %s analysis must be quit",
                        self.file_id,
                    )
                    self._terminate_process()
                    return

            if self.process.returncode == 0:
                result = self._parse_output(self.process.stdout.read())
                self.logger.debug("Thread stdout read, %s", result)
                signals.result_ready.emit(self.file_id, self.task_type, result)
            else:
                self.logger.error(
                    "Thread process return code, %s", self.process.returncode
                )
                signals.error_occurred.emit(
                    self.file_id, self.task_type, self.process.stderr.read()
                )
        except subprocess.CalledProcessError as e:
            error_msg = f"Exit code {e.returncode}: {e.stderr.strip()}"
            self.logger.debug("Thread CalledProcessError exception: %s", error_msg)
            signals.error_occurred.emit(self.file_id, self.task_type, error_msg)
        except Exception as e:
            self.logger.debug("Thread exception: %s", str(e))
            signals.error_occurred.emit(self.file_id, self.task_type, str(e))

    def terminate_process(self):
        """跨平台终止进程"""
        if self.process and self.process.poll() is None:
            if os.name == "nt":  # Windows
                self.logger.debug("Force quit analysis on Windows")
                self.process.send_signal(signal.CTRL_BREAK_EVENT)
                self.process.kill()
            else:  # Unix
                self.logger.debug("Force quit analysis on Unix")
                os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
            self.process.wait()

    def _build_command(self):
        """构建跨平台命令"""
        cmd = [self.program_path]
        cmd.extend(self.file_path)
        self.logger.debug("Build command: %s", cmd)
        """
        # Windows 路径处理
        if platform.system() == "Windows":
            for each_file_path in self.file_path:
                fastq_file_path = os.path.normpath(each_file_path).replace("/", "\\")
                self.logger.debug("Build command for Windows %s", fastq_file_path)
                cmd.append(fastq_file_path)
        else:
            cmd.extend(self.file_path)
        """
        return cmd

    def _parse_output(self, output):
        """解析程序输出"""
        self.logger.debug("Parse FASTQ file analysis result: %s", output)
        reads_match = re.search(r"Num reads:\s*(\d+)", output)
        bases_match = re.search(r"Num Bases:\s*(\d+)", output)
        q20_match = re.search(r"Q20\(%\):\s*(\d+\.\d+)", output)
        q30_match = re.search(r"Q30\(%\):\s*(\d+\.\d+)", output)

        if not reads_match or not bases_match:
            raise ValueError(
                "The format of output from cmd doesn't match the requirement"
            )

        if not q20_match or not q30_match:
            return {
                config.FASTQ_TOTAL_READS: int(reads_match.group(1)),
                config.FASTQ_TOTAL_BASES: int(bases_match.group(1)),
            }

        return {
            config.FASTQ_TOTAL_READS: int(reads_match.group(1)),
            config.FASTQ_TOTAL_BASES: int(bases_match.group(1)),
            config.FASTQ_PHRED_Q20: q20_match.group(1),
            config.FASTQ_PHRED_Q30: q30_match.group(1),
        }
