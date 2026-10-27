# --- 上一步明确了分组任务 → 这一块定义算法

# 创建解题类：符合 LeetCode 的要求
class Solution:

    # 定义分组函数：接收多个单词
    def groupAnagrams(self, words):

        # 创建空字典：保存不同的单词组
        groups_by_key = {}

        # --- 上一步拿到空字典 → 这一块逐个处理单词

        # 遍历单词列表：每次取出一个单词
        for word in words:

            # 对字母排序：让字母相同的词有相同顺序
            sorted_letters = sorted(word)

            # 连接排序后的字母：生成字典的键
            group_key = "".join(sorted_letters)

            # 检查字典：判断是否已有对应分组
            if group_key not in groups_by_key:

                # 新建空列表：用来保存这一组单词
                groups_by_key[group_key] = []

            # --- 上一步确定了分组 → 这一块保存当前单词

            # 把当前单词添加到对应组中
            groups_by_key[group_key].append(word)

        # 把字典里的所有分组取出来
        result = list(groups_by_key.values())

        # 返回最终分组：供测试函数检查
        return result


# --- 上一步写好了分组函数 → 这一块验证结果

# 定义测试函数：pytest 会自动执行
def test_array_hash_anagrams():

    # 设置测试数据：包含六个单词
    sample_words = [
        "eat", "tea", "tan",
        "ate", "nat", "bat"
    ]

    # 创建解题对象：用来调用算法
    solver = Solution()

    # 调用分组函数：获得计算结果
    grouped_words = solver.groupAnagrams(
        sample_words
    )

    # 打印结果：方便在终端观察
    print("分组结果：", grouped_words)

    # --- 上一步得到计算结果 → 这一块检查正确性

    # 设置正确答案：三个不同的组
    expected_groups = [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"]
    ]

    # 比较结果：相同说明测试通过
    assert grouped_words == expected_groups