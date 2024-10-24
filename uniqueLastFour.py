from matplotlib import pyplot as plt


def count_unique_last_four(text_file, keyword):
    last_four_count = {}

    with open(text_file, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if keyword in line:
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    if len(next_line) >= 5:
                        last_four = next_line[-5:]
                        if last_four not in last_four_count:
                            last_four_count[last_four] = 1
                        else:
                            last_four_count[last_four] += 1
            i += 1

    # 按出现次数高低排序结果
    sorted_result = sorted(last_four_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_result


if __name__ == "__main__":
    text_file = 'eth5.log'  # 替换为你的文本文件路径
    keyword = 'dengziqi'  # 替换为你的关键词

    result = count_unique_last_four(text_file, keyword)

    print("不同字符串数量：", len(result))
    print("不同字符串统计（按出现次数高低排序）：")
    for item in result:
        print(item[0], "-", item[1])

    # 提取前4位和频率作为绘图数据
    x = [item[0][:4] for item in result]
    y = [item[1] for item in result]

# 竖排输出字符串
    print("\n字符串频率统计：")
    for i in range(len(x)):
        print(f"{x[i]}")
    for i in range(len(x)):
        print(f"{y[i]}")