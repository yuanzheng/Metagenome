#include <iostream>
#include <string>
#include <zlib.h>
#include <thread>
#include <future>
#include <vector>

const int PHRED_OFFSET = 33;

struct FastqStats {
    size_t total_bases;
    size_t q20_bases;
    size_t q30_bases;

    FastqStats() : total_bases(0), q20_bases(0), q30_bases(0) {}
};

FastqStats analyze_fastq(const std::string& filename) {
    gzFile file = gzopen(filename.c_str(), "rb");
    FastqStats stats;

    if (!file) {
        std::cerr << "Error opening file: " << filename << std::endl;
        return stats;
    }

    char buffer[4096];
    int line_num = 0;

    while (gzgets(file, buffer, sizeof(buffer))) {
        line_num++;
        if (line_num % 4 == 0) {
            std::string qual_line(buffer);
            size_t end_pos = qual_line.find_last_not_of("\n\r");
            if (end_pos != std::string::npos) {
                qual_line = qual_line.substr(0, end_pos + 1);
            }

            for (size_t i = 0; i < qual_line.size(); ++i) {
                char c = qual_line[i];
                int phred = static_cast<int>(c) - PHRED_OFFSET;
                stats.total_bases++;
                if (phred > 20) stats.q20_bases++;
                if (phred > 30) stats.q30_bases++;
            }
        }
    }

    gzclose(file);
    return stats;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cout << "Usage: " << argv[0] << " <forward.fq.gz> <reverse.fq.gz>" << std::endl;
        return 1;
    }

    // 使用异步任务并行处理文件
    auto future_forward = std::async(std::launch::async, analyze_fastq, argv[1]);
    auto future_reverse = std::async(std::launch::async, analyze_fastq, argv[2]);

    // 等待并获取结果
    FastqStats fwd_stats = future_forward.get();
    FastqStats rev_stats = future_reverse.get();

    // 合并统计结果
    size_t total_bases = fwd_stats.total_bases + rev_stats.total_bases;
    size_t total_q20 = fwd_stats.q20_bases + rev_stats.q20_bases;
    size_t total_q30 = fwd_stats.q30_bases + rev_stats.q30_bases;

    // 输出结果
    std::cout.precision(2);
    std::cout << std::fixed;
    /*
    std::cout << "\n===== Parallel Processing Results =====" << std::endl;
    std::cout << "[Forward]" << std::endl;
    std::cout << "Total bases: " << fwd_stats.total_bases << std::endl;
    std::cout << "Q20: " << (fwd_stats.q20_bases * 100.0 / fwd_stats.total_bases) << "%" << std::endl;
    std::cout << "Q30: " << (fwd_stats.q30_bases * 100.0 / fwd_stats.total_bases) << "%\n" << std::endl;

    std::cout << "[Reverse]" << std::endl;
    std::cout << "Total bases: " << rev_stats.total_bases << std::endl;
    std::cout << "Q20: " << (rev_stats.q20_bases * 100.0 / rev_stats.total_bases) << "%" << std::endl;
    std::cout << "Q30: " << (rev_stats.q30_bases * 100.0 / rev_stats.total_bases) << "%\n" << std::endl;

    std::cout << "===== Combined Stats =====" << std::endl;
    std::cout << "Total bases: " << total_bases << std::endl;
    */
    std::cout << "Phred>Q20: " << (total_q20 * 100.0 / total_bases) << "%     ";
    std::cout << "Phred>Q30: " << (total_q30 * 100.0 / total_bases) << "%" << std::endl;

    return 0;
}
