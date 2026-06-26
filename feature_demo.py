"""
特征演示模块 —— 提供一些实用的工具函数。
"""


def calculate_average(numbers):
    """
    计算列表的平均值。

    参数:
        numbers: 一个数值列表（int 或 float）

    返回:
        float: 列表的平均值；若列表为空则返回 0.0
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    """
    计算列表的中位数。

    参数:
        numbers: 一个数值列表

    返回:
        float: 列表的中位数
    """
    if not numbers:
        return 0.0
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 1:
        return float(sorted_nums[mid])
    else:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2.0


if __name__ == "__main__":
    test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    avg = calculate_average(test_data)
    med = calculate_median(test_data)
    print(f"测试数据: {test_data}")
    print(f"平均值: {avg}")
    print(f"中位数: {med}")