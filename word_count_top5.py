import re
from collections import Counter

# 停止词列表（中英文常见词，可自行增减）
STOP_WORDS = {
    # 英文
    "is", "are", "was", "were", "am", "be", "been", "being",
    "he", "she", "it", "they", "i", "you", "we",
    "a", "an", "the", "this", "that", "these", "those",
    "in", "on", "at", "to", "for", "of", "from", "with",
    "and", "or", "but", "not", "so", "if", "as", "by",
    "do", "does", "did", "will", "would", "can", "could",
    "have", "has", "had", "my", "your", "his", "her", "our",
    "me", "him", "us", "them",
    # 中文
    "我", "你", "他", "她", "它", "我们", "你们", "他们", "她们",
    "的", "了", "在", "是", "有", "和", "就", "不", "都",
    "也", "这", "那", "要", "会", "很", "上", "下", "里",
    "吗", "吧", "呢", "啊", "哦", "嗯",
    "着", "过", "被", "把", "让", "给", "对", "向",
    "个", "之", "其", "所", "而", "且", "与", "或", "但",
    "一个", "什么", "怎么", "哪", "这个", "那个", "还", "没",
    "去", "来", "能", "做", "做", "说", "看", "想", "知道",
}


def count_words_top5(filepath, stop_words=None):
    """
    统计文本文件中每个单词的出现次数，过滤停止词后返回前5名。

    参数:
        filepath:   文本文件的路径
        stop_words: 停止词集合，默认为内置 STOP_WORDS

    返回:
        list[tuple]: 前5个 (单词, 次数) 的列表，按次数降序排列
    """
    if stop_words is None:
        stop_words = STOP_WORDS

    counter = Counter()
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line_lower = line.lower()
                # 匹配英文单词（纯字母）
                en_words = re.findall(r"[a-zA-Z]+", line_lower)
                # 匹配中文词（连续汉字，两字以上）
                zh_words = re.findall(r"[一-鿿]+", line)
                all_words = en_words + zh_words
                # 过滤掉停止词
                filtered = [w for w in all_words if w not in stop_words]
                counter.update(filtered)
    except FileNotFoundError:
        print(f"错误：文件 '{filepath}' 不存在。")
        return []

    return counter.most_common(5)


if __name__ == "__main__":
    result = count_words_top5("test")
    if result:
        print("出现次数最多的前5个单词：")
        for i, (word, count) in enumerate(result, 1):
            print(f"  {i}. {word} —— {count}次")
    else:
        print("未找到任何单词。")