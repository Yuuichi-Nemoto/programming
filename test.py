def calculate_sum(numbers):
    """
    リスト内の数値の合計を計算する関数。

    Parameters:
    numbers (list of int or float): 合計を計算する数値のリスト。

    Returns:
    int or float: 数値の合計。
    """
    total = 0
    for num in numbers:
        total += num
    return total

# サンプルのリストを定義
sample_list = [1, 2, 3, 4, 5]

# 関数を呼び出して合計を計算し、結果を表示
result = calculate_sum(sample_list)
print("合計は:", result)