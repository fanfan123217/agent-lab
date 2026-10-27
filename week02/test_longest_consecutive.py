# --- 上一步明确题目 → 这一块建立解题方法

# 创建解题类：符合 LeetCode 的调用要求
class Solution:

    # 定义方法：接收一个整数列表
    def longestConsecutive(self, numbers):

        # 转换为集合：去重并方便快速查找
        all_numbers = set(numbers)

        # 记录最长长度：初始为零
        longest_length = 0

        # --- 上一步拿到集合 → 这一块寻找序列起点

        # 遍历集合：检查每个数字
        for starting_number in all_numbers:

            # 前一个数字存在：说明当前不是起点
            if starting_number - 1 in all_numbers:

                # 跳过当前数字：避免重复计算
                continue

            # 保存起点：开始向后寻找连续数字
            current_number = starting_number

            # 起点算一个数字：初始长度为一
            current_length = 1

            # --- 上一步找到起点 → 这一块统计长度

            # 后一个数字存在：说明序列还能延长
            while current_number + 1 in all_numbers:

                # 移动到下一个数字：继续向后寻找
                current_number += 1

                # 长度增加一：记录新发现的数字
                current_length += 1

            # 更新最长记录：保留更大的长度
            longest_length = max(
                longest_length,
                current_length
            )

        # --- 上一步计算全部序列 → 这一块返回答案

        # 返回最终长度：题目不要求返回序列本身
        return longest_length


# --- 上一步完成算法 → 这一块测试计算结果

# 定义测试函数：让 pytest 自动执行
def test_array_hash_longest_sequence():

    # 准备乱序数字：包含连续的 1、2、3、4
    sample_numbers = [100, 4, 5, 1, 3, 2]

    # 创建解题对象：用于调用算法
    solver = Solution()

    # 计算最长连续序列：得到长度
    longest_length = solver.longestConsecutive(
        sample_numbers
    )

    # 打印答案：让我们看到计算结果
    print("最长连续序列长度：", longest_length)

    # 验证结果：最长序列长度应该为四
    assert longest_length == 5