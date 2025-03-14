from enum import Enum

from PySide6.QtCore import QObject, Signal


class TaskType(Enum):
    FASTQ_STATS = 1  # Tab1 的统计任务
    FASTQC_REPORT = 2  # Tab2 的FastQC任务


class GlobalSignals(QObject):
    started = Signal(str, TaskType)  # 任务开始信号（参数：文件对标识）
    result_ready = Signal(str, TaskType, dict)  # 分析结果信号（文件对标识，结果字典）
    error_occurred = Signal(str, TaskType, str)  # 错误信号（文件对标识，错误信息）


signals = GlobalSignals()
