from PySide6.QtCore import QThreadPool, QMutex, QMutexLocker
import config.config as config
import logging

# ==============================
# 全局控制标志（线程安全）
# ==============================
class AppState:
    def __init__(self):
        self.should_exit = False
        self.mutex = QMutex()
    
    # 线程安全地设置退出标志
    def request_exit(self):
        with QMutexLocker(self.mutex):  # 自动管理锁生命周期
            self.should_exit = True
    
    # 线程安全地获取退出标志
    def check_exit(self):
        with QMutexLocker(self.mutex):
            return self.should_exit

app_state = AppState()

class ThreadPoolManager:
    _instance = None
    
    def __new__(cls):
        if cls != ThreadPoolManager:
            raise TypeError("Singleton class cannot be inherited")
        
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.pool = QThreadPool.globalInstance()
            cls._instance.pool.setMaxThreadCount(config.FASTQ_MAX_THREAD_NUMBER)  # 限制最大并发数
            cls._instance.tasks = {}
            cls._instance.logger = logging.getLogger(cls.__class__.__name__)
        return cls._instance

    def submit_task(self, task_id, task):
        if task_id in self.tasks:
            self.logger.debug("Thread task %s already launched, so refuse this thread", task_id)
            return
        self.tasks[task_id] = task
        self.pool.start(task)

    def alive_thread_counter(self):
        self.logger.debug("Alive thread in the pool: %s", self.pool.activeThreadCount())
        return self.pool.activeThreadCount()

    def stop_all(self):
        for task in self.tasks.values():
            task.terminate_process()
        self.pool.waitForDone(2000)  # 最多等待2秒


