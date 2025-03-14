import csv
import logging
import threading
import time
from collections import defaultdict
from pathlib import Path

import constant_values.config as config


class CSVHandler:
    def __init__(self, csv_path, file_name):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.csv_file_path = Path(csv_path) / file_name
        self.data = defaultdict(dict)
        self._lock = threading.Lock()  # 线程锁
        self._ensure_directory_exists()
        self._load_existing_data()

    def _ensure_directory_exists(self):
        """确保目标目录存在"""
        try:
            self.csv_file_path.parent.mkdir(parents=True, exist_ok=True)
            self.logger.debug("Directory ready: %s", self.csv_file_path.parent)
        except Exception as e:
            self.logger.error("Create directory failed: %s", str(e))
            raise

    def _load_existing_data(self):
        if not self.csv_file_path.exists():
            return

        with open(self.csv_file_path, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                file_id = row[config.FASTQ_TOTAL_SAMPLEID]
                self.data[file_id] = row

    def has_file_id(self, file_id):
        return file_id in self.data

    def get_existing_data(self, file_id):
        return self.data.get(file_id)

    def append_result(self, file_id, field_names, field_data):
        retry = 3
        while retry > 0:
            try:
                with self._lock:  # 加锁保证原子操作
                    self.logger.debug("Start to write into csv file for %s", file_id)
                    row_data = {config.FASTQ_TOTAL_SAMPLEID: file_id}
                    row_data.update(field_data)

                    # 写入前先更新内存数据
                    self.data[file_id] = row_data

                    # 追加写入文件
                    file_exists = self.csv_file_path.exists()
                    with open(self.csv_file_path, "a", newline="") as f:
                        writer = csv.DictWriter(f, fieldnames=field_names)
                        if not file_exists:
                            writer.writeheader()
                        writer.writerow(row_data)
                    return
            except IOError as e:
                self.logger.error("Failed to write %s, caused by %s", file_id, e)
                retry -= 1
                time.sleep(0.1)
        else:
            self.logger.error("Failed to write %s after 3 retries", file_id)
