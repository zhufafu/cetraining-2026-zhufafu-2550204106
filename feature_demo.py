"""
feature_demo.py - 实验三：Git 分支与 Pull Request 练习
"""

def calculate_average(numbers):
    """计算列表的平均值

    Args:
        numbers: 一个包含数字的列表

    Returns:
        列表中所有数字的平均值，如果列表为空则返回 0
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    """计算列表的中位数

    Args:
        numbers: 一个包含数字的列表

    Returns:
        列表的中位数
    """
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]


if __name__ == "__main__":
    # 测试代码
    test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"测试数据: {test_data}")
    print(f"平均值: {calculate_average(test_data)}")
    print(f"中位数: {calculate_median(test_data)}")

    test_data2 = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"\n测试数据: {test_data2}")
    print(f"平均值: {calculate_average(test_data2)}")
    print(f"中位数: {calculate_median(test_data2)}")