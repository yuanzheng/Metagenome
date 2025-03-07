#include <zlib.h>
#include <iostream>
#include <string>
#include <future>
#include <mutex>

extern "C" {
#include "kseq.h"
}

KSEQ_INIT(gzFile, gzread)

// 存储统计结果的结构体
struct FastqStats {
    long reads = 0;
    long bases = 0;
    long q20 = 0;
    long q30 = 0;

    void merge(const FastqStats& other) {
        reads += other.reads;
        bases += other.bases;
        q20 += other.q20;
        q30 += other.q30;
    }
};

// 线程安全的统计结果累加器
class StatsCollector {
private:
    std::mutex mtx;
    FastqStats total;
public:
    void add(const FastqStats& stats) {
        std::lock_guard<std::mutex> lock(mtx);
        total.merge(stats);
    }

    void print() const {
        std::cout.precision(4);
        std::cout << "Num reads: " << total.reads << "\t"
                  << "Num Bases: " << total.bases << "\n"
                  << "Q20(%): " << (total.q20 * 100.0 / total.bases) << "\t"
                  << "Q30(%): " << (total.q30 * 100.0 / total.bases) << std::endl;
    }
};

// 处理单个FASTQ文件的函数
FastqStats analyze_file(const std::string& filename) {
    gzFile fp = gzopen(filename.c_str(), "r");
    FastqStats stats;
    
    if (!fp) {
        std::cerr << "Error opening: " << filename << std::endl;
        return stats;
    }

    kseq_t* seq = kseq_init(fp);
    int l;

    while ((l = kseq_read(seq)) >= 0) {  // 读取每条记录
        ++stats.reads;
        stats.bases += seq->seq.l;

        // 质量分析 (Phred+33编码)
        for (int i = 0; i < seq->qual.l; ++i) {
            int q = seq->qual.s[i] - 33;
            if (q > 20) ++stats.q20;
            if (q > 30) ++stats.q30;
        }
    }

    if (l == -2) std::cerr << "Truncated quality in: " << filename << std::endl;
    
    kseq_destroy(seq);
    gzclose(fp);
    return stats;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " forward.fq.gz reverse.fq.gz\n";
        return 1;
    }

    StatsCollector collector;

    // 并行处理函数
    auto process = [&collector](const char* file) {
        try {
            auto stats = analyze_file(file);
            collector.add(stats);
        } catch (...) {
            std::cerr << "Error processing: " << file << std::endl;
        }
    };

    // 启动异步任务
    auto f1 = std::async(std::launch::async, process, argv[1]);
    auto f2 = std::async(std::launch::async, process, argv[2]);

    // 等待任务完成
    f1.wait();
    f2.wait();

    // 输出最终结果
    collector.print();

    return 0;
}
