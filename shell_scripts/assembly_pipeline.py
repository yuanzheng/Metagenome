#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os
import re  # nosec
import subprocess  # nosec B404: 已通过安全封装处理
import sys  # nosec

import utils.system_utils as system_utils
from tqdm import tqdm


class FastQAssembly:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.paired_r1 = None
        self.paired_r2 = None
        self.unpaired = None
        self.output_dir = ""
        self.threads = 1
        self.min_contig_len = 500
        self._megahit_cmd = []

    def set_fastq_PE_input_files(self, input_dir):
        # 查找必需文件
        self.paired_r1 = system_utils.find_files(
            input_dir, ["R1_paired"], required=True
        )
        self.paired_r2 = system_utils.find_files(
            input_dir, ["R2_paired"], required=True
        )
        self.unpaired = system_utils.find_files(
            input_dir, ["R1_unpaired", "R2_unpaired"], required=False
        )

    def fastq_PE_files_are_valid(self):
        if not self.paired_r1 or not self.paired_r2:
            return False
        return True

    def set_output_dir(self, input_dir):
        base_name = os.path.basename(input_dir.rstrip(os.sep))
        self.output_dir = os.path.join(input_dir, f"{base_name}_assembly")

    def get_output_dir(self):
        return self.output_dir

    def set_thread_numbers(self, numbers):
        self.threads = numbers

    def set_min_contig_len(self, length):
        self.min_contig_len = length

    def build_megahit_cmd(self):
        self._megahit_cmd = [
            "megahit",
            "-1",
            self.paired_r1[0],
            "-2",
            self.paired_r2[0],
            "-o",
            self.output_dir,
            "-t",
            str(self.threads),
            "--min-contig-len",
            str(self.min_contig_len),
        ]
        if self.unpaired:
            self._megahit_cmd.extend(["-r", ",".join(self.unpaired)])

    def get_megahit_cmd(self):
        return self._megahit_cmd

    def print_cmd(self):
        print("\n将运行的命令:")
        print(" \\\n  ".join(self._megahit_cmd) + "\n")


def main():
    assembly_process = FastQAssembly()
    # 步骤1: 检查Megahit安装
    system_utils.check_tool_installed("megahit")

    try:
        while True:
            # 获取输入目录
            input_dir = system_utils.input_with_validation(
                "请输入trimmomatic输出目录绝对路径:",
                system_utils.validate_dir,
                "目录不存在，请重新输入。",
            )

            assembly_process.set_fastq_PE_input_files(input_dir)
            if not assembly_process.fastq_PE_files_are_valid():
                print("未找到必需的配对文件，请检查目录内容。")
            else:
                break

        # 创建输出目录
        assembly_process.set_output_dir(input_dir)

        # 获取线程数
        max_cpus = system_utils.get_cpu_core_numbers()
        try:
            threads = int(
                system_utils.input_positive_int(f"请输入线程数 (最大{max_cpus}): ")
                or max_cpus
            )
            threads = min(threads, max_cpus)
        except ValueError:
            threads = max_cpus
        assembly_process.set_thread_numbers(threads)

        # 获取最短contig长度
        try:
            min_contig_len = system_utils.input_positive_int("请输入最短contig长度: ")
        except ValueError:
            min_contig_len = 500
        assembly_process.set_min_contig_len(min_contig_len)

        # 构建命令
        assembly_process.build_megahit_cmd()

        # 显示命令
        assembly_process.print_cmd()

        # 确认运行
        if input("是否立即运行? (Y/N): ").upper() != "Y":
            print("退出程序。")
            sys.exit(0)

        # 运行并监控进度
        print("开始运行序列拼接...")
        process = subprocess.Popen(
            assembly_process.get_megahit_cmd(),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            bufsize=1,
        )

        # 初始化进度条参数
        total_k = None
        current_k = None
        processed_k = []
        k_list = []
        time_elapsed = None

        # 正则表达式模式
        k_list_pattern = re.compile(r"k-mer sizes:\s*\[([\d,\s]+)\]")
        k_start_pattern = re.compile(r"Assembling k=(\d+)")
        time_pattern = re.compile(r"Time elapsed:\s+([\d.]+)")

        with tqdm(total=100, desc="Assembly Progress", unit="%") as pbar:
            while True:
                line = process.stdout.readline()
                if not line:
                    if process.poll() is not None:
                        break
                    continue

                # 捕获k-mer列表
                if not k_list:
                    match = k_list_pattern.search(line)
                    if match:
                        k_list = [int(k.strip()) for k in match.group(1).split(",")]
                        total_k = len(k_list)
                        pbar.set_description(
                            f"Assembly Progress (k={max(k_list) if k_list else '?'})"
                        )
                        pbar.write(f"Detected k-mer list: {k_list}")

                # 捕获当前k值
                if not current_k:
                    match = k_start_pattern.search(line)
                    if match:
                        current_k = int(match.group(1))
                        processed_k.append(current_k)
                        progress = len(processed_k) / total_k * 100 if total_k else 0
                        pbar.update(progress - pbar.n)
                        pbar.set_description(f"Assembling k={current_k}")

                # 捕获时间信息
                time_match = time_pattern.search(line)
                if time_match:
                    time_elapsed = time_match.group(1)

                # 检测k值切换
                if "Final assembly" in line and total_k:
                    pbar.update(100 - pbar.n)
                    break
    except KeyboardInterrupt:
        print("\n用户中断, 退出程序。")
        sys.exit(1)

    # 步骤10: 显示时间
    if time_elapsed:
        print(f"\n总运行时间: {system_utils.format_time(time_elapsed)}")

    # 步骤11: 统计结果
    if input("\n是否统计组装结果? (Y/N): ").upper() == "Y":
        system_utils.check_tool_installed("seqkit")
        contig_file = os.path.join(
            assembly_process.get_output_dir(), "final.contigs.fa"
        )
        seqkit_cmd = ["seqkit", "stats", contig_file, "-N", "50", "-N", "90", "-T"]
        print("\n运行统计命令:")
        print(" ".join(seqkit_cmd))
        subprocess.run(seqkit_cmd)


if __name__ == "__main__":
    main()
