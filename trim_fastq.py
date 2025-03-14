import os
import subprocess  # nosec
import time


def validate_file(path):
    """验证文件路径是否存在且为文件"""
    if not os.path.exists(path):
        raise ValueError(f"路径 '{path}' 不存在")
    if not os.path.isfile(path):
        raise ValueError(f"'{path}' 是目录而不是文件")
    return path


def validate_dir(path):
    """验证目录路径，不存在则创建，存在则检查是否为目录"""
    if os.path.exists(path):
        if not os.path.isdir(path):
            raise ValueError(f"'{path}' 是文件而不是目录")
    else:
        try:
            os.makedirs(path, exist_ok=True)
        except Exception as e:
            raise ValueError(f"无法创建目录: {str(e)}")
    return path


def input_with_validation(prompt, validator, error_msg="无效输入，请重试"):
    """带验证的输入函数"""
    while True:
        try:
            value = input(prompt).strip()
            return validator(value)
        except ValueError as e:
            print(f"错误: {str(e)}")
            print(error_msg)


def input_positive_int(prompt):
    """输入正整数"""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("必须输入正整数")
        except ValueError:
            print("无效的输入，请输入整数")


def select_adapters():
    """选择接头文件"""
    adapter_dir = os.path.join("Trimmomatic-0.36", "adapters")

    # 验证适配器目录
    if not os.path.exists(adapter_dir):
        raise FileNotFoundError(f"适配器目录 '{adapter_dir}' 不存在")
    if not os.path.isdir(adapter_dir):
        raise ValueError(f"'{adapter_dir}' 不是目录")

    adapters = [
        f
        for f in os.listdir(adapter_dir)
        if os.path.isfile(os.path.join(adapter_dir, f))
    ]
    if not adapters:
        raise ValueError(f"适配器目录 '{adapter_dir}' 中没有可用文件")

    print("\n可用的接头文件:")
    for i, adapter in enumerate(adapters, 1):
        print(f"{i}. {adapter}")

    while True:
        try:
            choice = int(input("请选择接头文件（输入编号）: "))
            if 1 <= choice <= len(adapters):
                selected = adapters[choice - 1]
                return os.path.join(adapter_dir, selected)
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
            value = input_positive_int(f"请输入{options[choice][0]}: ")
            params[param_name] = str(value)
            params_order.append(param_name)

    return [(k, params[k]) for k in params_order]


def format_time(seconds: float) -> str:
    """格式化时间输出"""
    if seconds < 60:
        return f"{seconds:.1f}秒"
    minutes, sec = divmod(seconds, 60)
    return f"{int(minutes)}分{sec:.1f}秒"


def run_trimmomatic(cmd, out_dir):
    # 确认执行
    if input("\n是否执行? (Y/N): ").upper() == "Y":
        start_time = time.time()
        try:
            subprocess.run(cmd, shell=False, check=True)  # nosec
            print("\n处理完成！输出文件:")
            for f in os.listdir(out_dir):
                if f.endswith(".fq"):
                    print(f"- {os.path.join(out_dir, f)}")
        except subprocess.CalledProcessError as e:
            print(f"\n执行出错: {e}")

        # 耗时统计
        elapsed = time.time() - start_time
        print(f"\n任务完成 总耗时: {format_time(elapsed)}")
    else:
        print("\n已取消执行")


def main():
    print("=== Trimmomatic 质控程序 ===")

    # 读取基础参数
    while True:
        read_type = input("\n测序类型 (SE/PE): ").upper()
        if read_type in ["SE", "PE"]:
            break
        print("无效输入，请选择 SE 或 PE")

    # 输入文件路径
    if read_type == "PE":
        r1 = input_with_validation(
            "R1文件绝对路径: ", validate_file, "请确认文件存在且路径正确"
        )
        r2 = input_with_validation(
            "R2文件绝对路径: ", validate_file, "请确认文件存在且路径正确"
        )
    else:
        se = input_with_validation(
            "FASTQ文件绝对路径: ", validate_file, "请确认文件存在且路径正确"
        )

    # 输出目录
    out_dir = input_with_validation(
        "\n输出目录绝对路径: ", validate_dir, "请提供有效的目录路径"
    )

    # 接头参数
    try:
        adapter_file = select_adapters()
    except Exception as e:
        print(f"\n错误: {str(e)}")
        print("请检查Trimmomatic安装是否正确")
        return

    mismatch = input_positive_int("\n最大错配数: ")
    palindrome = input_positive_int("Palindrome阈值: ")
    simple = input_positive_int("Simple阈值: ")

    clip_params = [adapter_file, str(mismatch), str(palindrome), str(simple)]
    if input("\n添加更多接头参数? (y/N): ").lower() == "y":
        clip_params.append(str(input_positive_int("最短接头长度: ")))
        keep_both = input("保留双端? (true/false): ").lower()
        clip_params.append("true" if keep_both == "true" else "false")

    # 质量参数
    phred = (
        "phred33" if input("\n质量编码 (1:phred33, 2:phred64): ") == "1" else "phred64"
    )
    threads = input_positive_int("线程数: ")

    # 自定义参数
    custom_params = build_custom_params()

    # 构建命令
    cmd = [
        "java",
        "-jar",
        os.path.join("Trimmomatic-0.36", "trimmomatic-0.36.jar"),
        read_type,
        "-threads",
        str(threads),
        "-" + phred,
    ]

    # 添加输入输出文件
    if read_type == "PE":
        base = os.path.basename(r1).rsplit("_", 1)[0]
        cmd += [
            r1,
            r2,
            os.path.join(out_dir, f"{base}_R1_paired.fq"),
            os.path.join(out_dir, f"{base}_R1_unpaired.fq"),
            os.path.join(out_dir, f"{base}_R2_paired.fq"),
            os.path.join(out_dir, f"{base}_R2_unpaired.fq"),
        ]
    else:
        base = os.path.splitext(os.path.basename(se))[0]
        cmd += [se, os.path.join(out_dir, f"{base}_trimmed.fq")]

    # 添加处理参数
    cmd.append(f"ILLUMINACLIP:{':'.join(clip_params)}")
    for name, value in custom_params:
        cmd.append(f"{name}:{value}")

    # 显示最终命令
    print("\n生成命令:")
    print(" ".join(cmd))

    run_trimmomatic(cmd, out_dir)


if __name__ == "__main__":
    main()
