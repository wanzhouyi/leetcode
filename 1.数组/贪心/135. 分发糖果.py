"""
老师想给孩子们分发糖果，有 N个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
你需要按照以下要求，帮助老师给这些孩子分发糖果：
每个孩子至少分配到 1 个糖果。
评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

示例1：
输入：[1,0,2]
输出：5
解释：你可以分别给这三个孩子分发 2、1、2 颗糖果。

示例2：
输入：[1,2,2]
输出：4
解释：你可以分别给这三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这已满足上述两个条件。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/candy
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，两次遍历，84ms,44.39%
    def candy(self, ratings: List[int]) -> int:
        # 有 N 个孩子站成了一条直线
        n = len(ratings)
        # 每个孩子至少分配到 1 个糖果
        result = [1] * n
        for idx in range(1, n):
            if ratings[idx] > ratings[idx - 1]:
                result[idx] = result[idx - 1] + 1
        for idx in range(n - 2, -1, -1):
            if ratings[idx] > ratings[idx + 1]:
                result[idx] = result[idx + 1] + 1 if result[idx] <= result[idx + 1] else result[idx]
        return sum(result)


if __name__ == '__main__':
    s = Solution()
    # 官方用例
    print(s.candy([1, 0, 2]))
    print(s.candy([1, 2, 2]))
    # 空数组
    print(s.candy([]))
    # 一个元素
    print(s.candy([1]))
    # 全一样的元素
    print(s.candy([1] * 10))
    # 递增
    print(s.candy([i for i in range(1, 10)]))
    # 递减
    print(s.candy([i for i in range(9, 0, -1)]))
    # 拱桥形数组
    print(s.candy([1, 2, 3, 2, 1]))
