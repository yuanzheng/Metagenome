#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

import utils.system_utils as system_utils
from assembly_fastq_app import assembly_contig_length, assembly_main
from trim_fastq_app import trimmomatic_main

from utils.logging.logging_config import setup_logger

setup_logger()

if __name__ == "__main__":
    try:
        # 获取FASTQ样本目录
        samples_dir = system_utils.input_with_validation(
            "请输入样本FASTQ文件所在目录(绝对路径):",
            system_utils.validate_dir,
            "目录不存在，请重新输入。",
        )
    except KeyboardInterrupt:
        print("\n用户中断, 退出程序。")
        sys.exit(1)
    except Exception as e:
        print(f"出错, {e} \n退出程序")
        sys.exit(1)

    try:
        while True:
            options = {
                "1": "清洗一组FASTQ数据",
                "2": "组装数据（序列拼接）",
                "3": "组装序列长度分布图",
                "4": "退出",
            }

            print("\n\n")
            for key, value in options.items():
                print(f"{key}: {value}")

            choice = "1"
            while True:
                choice = input("请输入序号 (1-4): ").strip().lower()
                if choice in options:
                    break
                print("无效的序号")
            try:
                if choice == "1":
                    trimmomatic_main(samples_dir)
                elif choice == "2":
                    assembly_main()
                elif choice == "3":
                    assembly_contig_length(samples_dir)
                elif choice == "4":
                    break
            except Exception as e:
                print(f"错误: {e}")
    except KeyboardInterrupt:
        print("\n用户中断, 退出程序。")
        sys.exit(1)
