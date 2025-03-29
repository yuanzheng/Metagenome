import os
import time

import utils.system_utils as system_utils
from trimmomatic.fastq_trimmomatic import FastQTrimmomatic


def select_adapters(adapters):
    print("\n可用的接头文件:")
    for i, adapter in enumerate(adapters, 1):
        print(f"{i}. {adapter}")

    while True:
        try:
            choice = int(input("请选择接头文件（输入编号）: "))
            if 1 <= choice <= len(adapters):
                return adapters[choice - 1]
            print(f"请输入1-{len(adapters)}之间的编号")
        except ValueError:
            print("请输入有效数字")


def build_custom_params():
    """构建自定义参数"""
    params_order = []
    params = {}
    options = {
        "1": ("LEADING", "质量阈值"),
        "2": ("TRAILING", "质量阈值"),
        "3": ("MAXNN", "最大N数"),
        "4": ("MINLEN", "最小长度"),
        "5": ("SLIDINGWINDOW", "窗口大小 质量阈值"),
        "6": ("CROP", "保留长度"),
        "7": ("HEADCROP", "切除长度"),
    }

    print("\n可选参数（输入序号或done结束）:")
    for key, value in options.items():
        print(f"{key}: {value[0]}")

    while True:
        choice = input("请输入参数序号 (1-7): ").strip().lower()
        if choice == "done":
            break
        if choice not in options:
            print("无效的序号")
            continue
        if choice in params:
            print("该参数已添加")
            continue

        param_name = options[choice][0]
        if choice == "5":
            while True:
                try:
                    values = input(
                        "输入SLIDINGWINDOW, 窗口大小和平均质量（用空格分隔）: "
                    ).split()
                    if len(values) != 2:
                        raise ValueError
                    win, qual = map(int, values)
                    if win <= 0 or qual <= 0:
                        raise ValueError
                    params[param_name] = f"{win}:{qual}"
                    params_order.append(param_name)
                    break
                except Exception as e:
                    print(f"无效输入，示例: 4 20, {e}")
        else:
            value = system_utils.input_positive_int(f"请输入{options[choice][0]}: ")
            params[param_name] = str(value)
            params_order.append(param_name)

    return [(k, params[k]) for k in params_order]


def trimmomatic_main():
    print("\n=== Trimmomatic 质控程序 ===")
    trim_process = FastQTrimmomatic()

    try:
        # 读取基础参数
        while True:
            read_type = input("测序类型 (SE/PE): ").upper()
            if read_type in ["SE", "PE"]:
                trim_process.set_mode(read_type)
                break
            print("无效输入，请选择 SE 或 PE")

        # 输入文件路径
        if read_type == "PE":
            r1 = system_utils.input_with_validation(
                "R1文件绝对路径: ",
                system_utils.validate_file,
                "请确认文件存在且路径正确",
            )
            r2 = system_utils.input_with_validation(
                "R2文件绝对路径: ",
                system_utils.validate_file,
                "请确认文件存在且路径正确",
            )
            trim_process.set_forword_file(r1)
            trim_process.set_reverse_file(r2)
        else:
            se = system_utils.input_with_validation(
                "FASTQ文件绝对路径: ",
                system_utils.validate_file,
                "请确认文件存在且路径正确",
            )
            trim_process.set_single_end_file(se)

        # 输出目录
        out_dir = system_utils.input_with_validation(
            "\n输出目录绝对路径: ",
            system_utils.validate_dir_and_mkdir,
            "请提供有效的目录路径",
        )
        trim_process.set_output_dir(out_dir)

        # 接头参数
        adapter_file = select_adapters(trim_process.get_adapter_options())
        trim_process.set_adapter_file(adapter_file)

        mismatch = system_utils.input_positive_int("\n最大错配数: ")
        palindrome = system_utils.input_positive_int("Palindrome阈值: ")
        simple = system_utils.input_positive_int("Simple阈值: ")
        trim_process.set_seed_mismatches(mismatch)
        trim_process.set_palindrome_clip_threshold(palindrome)
        trim_process.set_simple_clip_threshold(simple)

        if input("\n添加更多接头参数? (y/N): ").lower() == "y":
            trim_process.set_min_prefix(
                system_utils.input_positive_int("最短接头长度: ")
            )
            trim_process.set_palindrome_keep_booth(
                system_utils.input_str("保留双端? (true/false): ").lower()
            )

        # 质量参数
        phred_option = phred = input(
            "\n质量编码 (1:phred33, 2:phred64), 或放弃添加直接回车键: "
        )
        if phred_option != "":
            phred = "-phred33" if phred_option == "1" else "-phred64"
            trim_process.set_phred_option(phred)

        threads = system_utils.input_positive_int("线程数: ")
        trim_process.set_threads(threads)

        # 自定义参数
        custom_params = build_custom_params()
        trim_process.set_custom_params(custom_params)

        cmd = trim_process._build_cmd()

        # 显示最终命令
        print("\n生成命令:")
        print(" ".join(cmd))

        # 确认执行
        if input("\n是否执行? (Y/N): ").upper() == "Y":
            start_time = time.time()
            trim_process.run_trim_process()
            print("\n处理完成! 输出文件:")
            for file in os.listdir(trim_process.get_output_dir()):
                if file.endswith(".fq.gz"):
                    print(f"- {os.path.join(trim_process.get_output_dir(), file)}")
            # 耗时统计
            elapsed = time.time() - start_time
            print(f"\n任务完成 总耗时: {system_utils.format_time(elapsed)}")
            print(f"查看输出目录: {out_dir}")
        else:
            print("\n已取消执行")
    except KeyboardInterrupt:
        print("\n用户中断, 退出清洗程序。")
    except Exception as e:
        raise RuntimeError("清洗过程出错") from e
