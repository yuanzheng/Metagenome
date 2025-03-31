import os

import utils.system_utils as system_utils
from assembly.fastq_assembly import FastQAssembly


def print_stats_result(data):
    # 提取字段
    stats = {
        "num_seqs": data[3],
        "sum_len": data[4],
        "min_len": data[5],
        "max_len": data[7],
        "N50": data[8],
        "N90": data[9],
    }

    # 提取SampleID
    file_path = data[0]
    base_dir = os.path.basename(os.path.dirname(os.path.dirname(file_path)))
    sample_id = base_dir.split("_")[0]

    # 格式化输出
    print(f"SampleID: {sample_id}")
    print(f"Number:   {stats['num_seqs']:>10}")
    print(f"Lenght:   {stats['sum_len']:>12}")
    print(f"N50:      {stats['N50']:>8}")
    print(f"N90:      {stats['N90']:>8}")
    print(f"Max:      {stats['max_len']:>8}")
    print(f"Min:      {stats['min_len']:>8}")


def assembly_main():
    print("=== Megahit 组装程序 ===")
    assembly_process = FastQAssembly()
    # TODO 未来需要更灵活一些，给出参数
    seqkit_params = ["-N", "50", "-N", "90", "-T"]
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
                print(f"megahit: 输出目录 {output_dir} 已经存在, 所以直接统计结果")
                # 统计结果
                lines = assembly_process.stats(seqkit_params)
                # 解析输出
                data = lines[1].split("\t")
                print_stats_result(data)
                return
        except ValueError:
            print("")  # assembly output directory must not be existed

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
        print("\n将运行的命令:")
        print(" \\\n  ".join(assembly_process.get_megahit_cmd()) + "\n")

        # 确认运行
        if input("是否立即运行? (Y/N): ").upper() != "Y":
            print("退出组装。")
            return

        # 检查Megahit安装
        system_utils.check_tool_installed("megahit")

        print("开始运行序列拼接...")
        assembly_process.start_megahit_assembly(True)

        # 统计结果
        if input("\n是否统计组装结果? (Y/N): ").upper() == "Y":
            lines = assembly_process.stats(seqkit_params)
            # 解析输出
            data = lines[1].split("\t")
            print_stats_result(data)

    except KeyboardInterrupt:
        print("\n用户中断, 退出组装程序。")
    except Exception as e:
        print(f"组装过程出错, {e}")


def assembly_contig_length(samples_dir: str):
    try:
        print("=== 组装结果contig长度分布图 ===")
    except KeyboardInterrupt:
        print("\n用户中断, 退出生成柱状图(contig distribution)程序。")
    except Exception as e:
        print(f"生成柱状图(contig distribution)过程出错, {e}")
