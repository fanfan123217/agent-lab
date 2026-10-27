# --- 上一步明确了题目输入 → 这一块建立解题方法

# 定义解题类：LeetCode 会寻找 Solution
class Solution:

    # 定义解题方法：接收数字列表与目标和
    def twoSum(self, numbers, target_sum):

        # 创建空字典：记录见过的数字及下标
        seen_positions = {}

        # --- 上一步拿到空字典 → 这一块逐个寻找配对数字

        # 同时取得位置和值：方便返回两个下标
        for index, number in enumerate(numbers):

            # 计算缺少的数字：两数相加要等于目标
            needed_number = target_sum - number

            # 检查字典：看之前有没有见过所需数字
            if needed_number in seen_positions:

                # 找回旧数字的位置：组成答案
                old_index = seen_positions[needed_number]

                # 返回两个下标：题目需要的是位置
                return [old_index, index]

            # 记录当前数字：供后面的数字查询
            seen_positions[number] = index

        # --- 上一步查完所有数字 → 这一块处理没有答案的情况

        # 返回空列表：避免找不到时没有返回值
        return []


# --- 上一步写好解题方法 → 这一块验证样例

# 定义测试函数：pytest 会自动找到它
def test_array_hash_two_sum():

    # 准备测试数字：这里包含 2 和 7
    sample_numbers = [3, 2, 4]

    # 设置目标和：2 加 7 等于 9
    target_sum = 6

    # 建立解题对象：用于调用方法
    solver = Solution()

    # 调用算法：计算答案对应的下标
    found_positions = solver.twoSum(
        # 传入数字和目标值：验证上面的算法
        sample_numbers, target_sum
    )
    print("两数之和的下标是：", found_positions)
    # 检查结果：正确的下标应是 0 和 1
    assert found_positions == [1, 2]
    