import logging
FASTQC_REPORT_DIRECTORY = "fastQCreport"
FASTQ_DATA_DIRECTORY = ""
FASTQ_PARSER_EXE_FILE = ""
FASTQ_ANALYSIS_REPORT_DIRECTORY = "fastQ_analysis"
FASTQ_TOTAL_READS = "Total_Reads"
FASTQ_TOTAL_BASES = "Total_Bases"
FASTQ_PHRED_Q20 = "Q20"
FASTQ_PHRED_Q30 = "Q30"
FASTQ_TOTAL_SAMPLEID = "样本ID"
FASTQC_REPORT_EXTENSION = ".zip"
FASTQ_FILE_EXTENSION = ".fastq.gz"
FASTQ_MAX_THREAD_NUMBER = 2
FASTQC_REPORT_IMAGE_SEQUENCE_QUALITY = "per_base_quality.svg"
FASTQC_REPORT_IMAGE_SEQUENCE_CONTENT = "per_base_sequence_content.svg"
LOGGING_LEVEL = logging.DEBUG
SETUP_MODULE_LOGGING_LEVEL = logging.DEBUG
# 保存所有线程
threads = []
