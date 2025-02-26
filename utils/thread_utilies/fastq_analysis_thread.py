import sys
import os
import re
import platform
import subprocess
import logging
import config.config as config
from PySide6.QtCore import QRunnable, Signal, QObject

# ==============================
# 信号容器（用于跨线程通信）
# ==============================
class AnalysisSignals(QObject):
    started = Signal(str)           # 任务开始信号（参数：文件对标识）
    result_ready = Signal(str, dict) # 分析结果信号（文件对标识，结果字典）
    error_occurred = Signal(str, str) # 错误信号（文件对标识，错误信息）


# ==============================
# 可执行分析任务线程
# ==============================
class AnalysisTask(QRunnable):
    
    def __init__(self, file_id, file_path, program_path):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.file_id = file_id  # MT37
        self.file_path = file_path  # (R1路径, R2路径)
        self.program_path = program_path
        self.signals = AnalysisSignals()
        self.setAutoDelete(True)   # 任务完成后自动清理

    def run(self):
        self.signals.started.emit(self.file_id)

        try:
            self.logger.info("Start fastQ analysis thread!")

            # 构造跨平台命令
            cmd = self._build_command()

            # 执行外部程序
            result = subprocess.run(
                cmd,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                creationflags=subprocess.CREATE_NO_WINDOW if platform.system() == "Windows" else 0
            )
            
            # 解析输出
            stats = self._parse_output(result.stdout)
            self.signals.result_ready.emit(self.file_id, stats)
        except subprocess.CalledProcessError as e:
            error_msg = f"Exit code {e.returncode}: {e.stderr.strip()}"
            self.signals.error_occurred.emit(self.file_id, error_msg)
        except Exception as e:
            self.signals.error_occurred.emit(self.file_id, str(e))

    def _build_command(self):
        """构建跨平台命令"""
        cmd = [self.program_path]
        cmd.extend(self.file_path)
        self.logger.debug("Build command: %s", cmd)
        '''
        # Windows 路径处理
        if platform.system() == "Windows":
            for each_file_path in self.file_path:
                fastq_file_path = os.path.normpath(each_file_path).replace("/", "\\")
                self.logger.debug("Build command for Windows %s", fastq_file_path)
                cmd.append(fastq_file_path)
        else:
            cmd.extend(self.file_path)
        '''
        return cmd

    def _parse_output(self, output):
        """解析程序输出"""
        self.logger.debug("Parse FASTQ file analysis result: %s", output)
        reads_match = re.search(r"Num reads:\s*(\d+)", output)
        bases_match = re.search(r"Num Bases:\s*(\d+)", output)
        
        if not reads_match or not bases_match:
            raise ValueError("输出格式不符合预期")
            
        return {
            config.FASTQ_TOTAL_READS: int(reads_match.group(1)),
            config.FASTQ_TOTAL_BASES: int(bases_match.group(1))
        }