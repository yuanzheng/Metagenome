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

    def stats(self):
        system_utils.check_tool_installed("seqkit")
        contig_file = os.path.join(self.output_dir, "final.contigs.fa")
        seqkit_cmd = ["seqkit", "stats", contig_file, "-N", "50", "-N", "90", "-T"]
        print("\n运行统计命令:")
        print(" ".join(seqkit_cmd))
        subprocess.run(seqkit_cmd)

    def start_megahit_assembly(self):
        if not self._megahit_cmd:
            print("megahit command doesn't exist")
        # 运行并监控进度
        print("开始运行序列拼接...")
        process = subprocess.Popen(
            self._megahit_cmd,
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
        k_list_pattern = re.compile(r"k list:\s*(\d+(?:,\s*\d+)*)")
        k_start_pattern = re.compile(r"Assemble contigs from SdBG for k\s*=\s*(\d+)")
        time_pattern = re.compile(r"Time elapsed:\s+([\d.]+)")

        with tqdm(
            total=100,
            desc="序列拼接进度",
            unit="%",
            bar_format="{desc}{bar:60}| {n:.0f}% {postfix} [剩余时间:{remaining}]",
            ncols=100,  # 控制进度条宽度
            mininterval=0.3,
        ) as pbar:
            while True:
                line = process.stdout.readline()
                if not line:
                    if process.poll() is not None:
                        break
                    continue

                # 捕获k-list列表
                if "k list" in line:
                    match = k_list_pattern.search(line)
                    if match:
                        k_list = [int(k.strip()) for k in match.group(1).split(",")]
                        total_k = len(k_list) + 1
                        pbar.update(2 - pbar.n)
                        pbar.set_description(f"序列拼接进度 (共{len(k_list)}个)")
                        pbar.write(f"Detected k list: {k_list}")

                # 捕获当前k值
                if "Assemble contigs" in line:
                    match = k_start_pattern.search(line)
                    if match:
                        current_k = int(match.group(1))
                        if current_k in k_list and current_k not in processed_k:
                            processed_k.append(current_k)
                            progress = (
                                int(round(len(processed_k) / total_k * 100))
                                if total_k
                                else 0
                            )
                            pbar.update(progress - pbar.n)
                            pbar.set_postfix_str(f"当前k值: {current_k}", refresh=True)

                # 捕获时间信息
                if "ALL DONE" in line:
                    time_match = time_pattern.search(line)
                    if time_match:
                        time_elapsed = time_match.group(1)
                    pbar.update(100 - pbar.n)
                    break
        pbar.close()
        # 显示时间
        if time_elapsed:
            print(f"\n总运行时间: {system_utils.format_time(float(time_elapsed))}")


def main():
    assembly_process = FastQAssembly()
    # 检查Megahit安装
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
        try:
            output_dir = system_utils.validate_dir(assembly_process.get_output_dir())
            if output_dir:
                print(f"megahit: 输出目录 {output_dir} 已经存在, 所以可以开始统计结果")
                # 统计结果
                assembly_process.stats()
                sys.exit(0)
        except ValueError:
            print("")

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
        assembly_process.start_megahit_assembly()
    except KeyboardInterrupt:
        print("\n用户中断, 退出程序。")
        sys.exit(1)

    # 统计结果
    if input("\n是否统计组装结果? (Y/N): ").upper() == "Y":
        assembly_process.stats()


if __name__ == "__main__":
    main()
