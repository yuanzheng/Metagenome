import logging
import os
import subprocess  # nosec
from pathlib import Path


class FastQTrimmomatic:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self._mode = "PE"  # PE or SE，默认为PE
        self._forword_file_path = None
        self._reverse_file_path = None
        self._single_end_file_path = None
        self._output_dir = None
        self._trimmomatic_jar = None
        self._adapters_dir = None
        self._adapter_options = []  # list all adapters
        self._adapter_file = None  # selected adapter
        self._seed_mismatches = None
        self._palindrome_clip_threshold = None
        self._simple_clip_threshold = None
        self._minPrefix = None
        self._palindromeKeepBoth = None
        self._phred_option = None
        self._threads = None
        self._custom_params = None
        self.init_trim_adapter()

    def init_trim_adapter(self):
        try:
            self._trimmomatic_jar, self._adapters_dir = self.get_trimmomatic_paths()
            self._adapter_options = [
                file
                for file in os.listdir(self._adapters_dir)
                if os.path.isfile(os.path.join(self._adapters_dir, file))
            ]
            if not self._adapter_options:
                raise ValueError(
                    f"Trimommatic适配器目录 '{self._adapters_dir}' 中没有可用文件"
                )
        except Exception as e:
            self.logger.error(f"\n错误: {str(e)}")
            self.logger.error("请检查Trimmomatic安装是否正确")
            raise RuntimeError("系统中没有找到足够的Trimommatic安装信息") from e

    def get_adapter_options(self):
        return self._adapter_options

    def get_adapters_dir(self):
        return self.adapters_dir

    def _find_system_trimmomatic(self):
        """检查系统是否安装Trimmomatic并返回路径"""
        self.logger.debug("检查which命令(Unix系统)")
        if os.name != "nt":
            trimmomatic_bin = (
                subprocess.check_output(
                    ["which", "trimmomatic"], stderr=subprocess.DEVNULL
                )
                .decode()
                .strip()
            )
            if trimmomatic_bin:
                jar_path = Path(trimmomatic_bin).resolve().parent / "trimmomatic.jar"
                adapters_dir = jar_path.parent / "adapters"
                if jar_path.exists():
                    return str(jar_path), str(adapters_dir)

        self.logger.debug("检查环境变量")
        env_path = os.environ.get("TRIMMOMATIC_HOME")
        if env_path:
            jar_path = Path(env_path) / "trimmomatic.jar"
            adapters_dir = Path(env_path) / "adapters"
            if jar_path.exists() and adapters_dir.exists():
                return str(jar_path), str(adapters_dir)

        self.logger.debug("检查常见安装路径")
        common_paths = [
            "/usr/share/trimmomatic",
            "/usr/local/trimmomatic",
            "/opt/trimmomatic",
            Path.home() / ".local/share/trimmomatic",
        ]

        for path in common_paths:
            p = Path(path)
            jar = p / "trimmomatic.jar"
            adapters = p / "adapters"
            if jar.exists() and adapters.exists():
                return str(jar), str(adapters)

        return None, None

    def get_trimmomatic_paths(self):
        """获取Trimmomatic路径"""
        # 优先使用系统安装版本
        try:
            sys_jar, sys_adapters = self._find_system_trimmomatic()
            if sys_jar:
                self.logger.info(f"检测到系统安装的Trimmomatic: {sys_jar}")
                return sys_jar, sys_adapters
        except Exception:
            print("")

        # 使用自带版本
        local_jar = os.path.join("../Trimmomatic-0.36", "trimmomatic-0.36.jar")
        """选择接头文件"""
        local_adapters = os.path.join("../Trimmomatic-0.36", "adapters")

        if not os.path.exists(local_jar):
            raise FileNotFoundError(
                f"错误: 未找到Trimmomatic JAR文件, 请确保存在 '{local_jar}'"
            )

        # 验证适配器目录
        if not os.path.exists(local_adapters):
            raise FileNotFoundError(f"适配器目录 '{local_adapters}' 不存在")

        if not os.path.isdir(local_adapters):
            raise ValueError(f"'{local_adapters}' 不是目录")

        self.logger.info("使用自带的Trimmomatic版本")
        return local_jar, local_adapters

    def set_mode(self, mode):
        self._mode = mode

    def set_forword_file(self, file_path):
        self._forword_file_path = file_path

    def set_reverse_file(self, file_path):
        self._reverse_file_path = file_path

    def set_single_end_file(self, file_path):
        self._single_end_file_path = file_path

    def set_output_dir(self, dir):
        self._output_dir = dir

    def get_output_dir(self):
        return self._output_dir

    def set_adapter_file(self, file_name):
        if self._adapters_dir is None:
            raise ValueError("Trimmomatic adapters directory was not initialized")
        self._adapter_file = os.path.join(self._adapters_dir, file_name)

    def set_seed_mismatches(self, value):
        self._seed_mismatches = value

    def set_palindrome_clip_threshold(self, value):
        self._palindrome_clip_threshold = value

    def set_simple_clip_threshold(self, value):
        self._simple_clip_threshold = value

    def set_min_prefix(self, value):
        self._minPrefix = value

    def set_palindrome_keep_booth(self, value):
        self._palindromeKeepBoth = value

    def set_phred_option(self, value):
        self._phred_option = value

    def set_threads(self, value):
        self._threads = value

    def set_custom_params(self, custom_params):
        self._custom_params = custom_params

    def _build_cmd(self):
        # 构建命令
        cmd = [
            "java",
            "-jar",
            self._trimmomatic_jar,
            self._mode,
            "-threads",
            str(self._threads),
        ]

        if self._phred_option is not None:
            cmd += [
                self._phred_option,
            ]

        # 添加输入输出文件
        cmd += self.get_input_output_params()

        # 添加处理参数
        cmd.append(self.get_illuminaclip_params())
        for name, value in self._custom_params:
            cmd.append(f"{name}:{value}")

        return cmd

    def get_illuminaclip_params(self):
        clip_params = [
            self._adapter_file,
            str(self._seed_mismatches),
            str(self._palindrome_clip_threshold),
            str(self._simple_clip_threshold),
        ]
        if self._minPrefix is not None:
            clip_params.append(str(self._minPrefix))
        if self._palindromeKeepBoth is not None:
            clip_params.append(
                "true" if self._palindromeKeepBoth == "true" else "false"
            )

        return f"ILLUMINACLIP:{':'.join(clip_params)}"

    def get_input_output_params(self):
        if self._mode == "PE":
            base = os.path.basename(self._forword_file_path).rsplit("_", 1)[0]
            return [
                self._forword_file_path,
                self._reverse_file_path,
                os.path.join(self._output_dir, f"{base}_R1_paired.fq.gz"),
                os.path.join(self._output_dir, f"{base}_R1_unpaired.fq.gz"),
                os.path.join(self._output_dir, f"{base}_R2_paired.fq.gz"),
                os.path.join(self._output_dir, f"{base}_R2_unpaired.fq.gz"),
            ]

        base = os.path.splitext(os.path.basename(self._single_end_file_path))[0]
        return [
            self._single_end_file_path,
            os.path.join(self._output_dir, f"{base}_trimmed.fq.gz"),
        ]

    def run_trim_process(self):
        try:
            subprocess.run(self._build_cmd(), shell=False, check=True)  # nosec
            self.logger.info("\n处理完成! 输出文件:")
            for file in os.listdir(self._output_dir):
                if file.endswith(".fq"):
                    self.logger.info(f"- {os.path.join(self._output_dir, file)}")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"\n执行出错: {e}")
            raise
