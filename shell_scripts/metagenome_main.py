#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from assembly_fastq_app import assembly_main
from trim_fastq_app import trimmomatic_main

from utils.logging.logging_config import setup_logger

setup_logger()

if __name__ == "__main__":
    try:
        while True:
            options = {
                "1": "清洗一组FASTQ数据",
                "2": "组装数据（序列拼接）",
                "3": "退出",
            }

            print("\n\n")
            for key, value in options.items():
                print(f"{key}: {value}")

            choice = "1"
            while True:
                choice = input("请输入序号 (1-3): ").strip().lower()
                if choice in options:
                    break
                print("无效的序号")
            try:
                if choice == "1":
                    trimmomatic_main()
                elif choice == "2":
                    assembly_main()
                elif choice == "3":
                    break
            except Exception as e:
                print(f"错误: {e}")
    except KeyboardInterrupt:
        print("\n用户中断, 退出程序。")
        sys.exit(1)
