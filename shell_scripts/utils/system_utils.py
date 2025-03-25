import os
import shutil
import sys


def get_cpu_core_numbers():
    return os.cpu_count() or 1


def check_tool_installed(tool_name):
    if shutil.which(tool_name) is None:
        print(f"错误: 未安装 {tool_name}，请先安装后再运行本程序。")
        sys.exit(1)


def find_files(directory, patterns, required=True):
    found_files = []
    for pattern in patterns:
        matches = [
            f
            for f in os.listdir(directory)
            if pattern in f and os.path.isfile(os.path.join(directory, f))
        ]
        if required and not matches:
            return None
        found_files.extend(matches)
    return [os.path.join(directory, f) for f in found_files] if found_files else []


def validate_dir(path):
    """验证目录路径，不存在则创建，存在则检查是否为目录"""
    if os.path.exists(path):
        if not os.path.isdir(path):
            raise ValueError(f"'{path}' 是文件而不是目录")
    else:
        raise ValueError(f"{path}")
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


def format_time(seconds: float) -> str:
    """格式化时间输出"""
    if seconds < 60:
        return f"{seconds:.1f}秒"

    minutes, sec = divmod(seconds, 60)
    if minutes < 60:
        return f"{int(minutes)}分{sec:.1f}秒"

    hours, min = divmod(minutes, 60)
    return f"{int(hours)}小时{int(min)}分{sec:.1f}秒"
