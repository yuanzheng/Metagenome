import logging
import os
import re  # nosec
import subprocess  # nosec B404: 已通过安全封装处理

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

    def _build_stats_cmd(self, param_list=None):
        system_utils.check_tool_installed("seqkit")
        contig_file = os.path.join(self.output_dir, "final.contigs.fa")
        seqkit_cmd = [
            "seqkit",
            "stats",
            contig_file,
        ]
        if param_list:
            seqkit_cmd += param_list

        return seqkit_cmd

    def stats(self, param_list=None):
        try:
            seqkit_cmd = self._build_stats_cmd(param_list)
            self.logger.info("运行统计命令:")
            self.logger.info(" ".join(seqkit_cmd))
            result = subprocess.run(
                seqkit_cmd, capture_output=True, text=True, check=True
            )
            return result.stdout.strip().split("\n")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"执行出错: {e}")
            raise RuntimeError(f"seqkit 执行出错: {e}") from e
        except RuntimeError as e:
            self.logger.error(f"执行出错: {e}")
            raise Exception(f"执行出错: {e}") from e

    def start_megahit_assembly(self):
        if not self._megahit_cmd:
            self.logger.error("megahit command doesn't exist")
            raise ValueError("megahit command doesn't exist")
        # 运行并监控进度
        try:
            self.logger.info("开始运行序列拼接...")
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
            k_start_pattern = re.compile(
                r"Assemble contigs from SdBG for k\s*=\s*(\d+)"
            )
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
                                pbar.set_postfix_str(
                                    f"当前k值: {current_k}", refresh=True
                                )

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
        except subprocess.CalledProcessError as e:
            self.logger.error(f"\nMegahit序列拼接 - 执行出错: {e}")
            raise
        except Exception as e:
            self.logger.error(f"\nMegahit序列拼接 - 执行出错: {e}")
            raise
