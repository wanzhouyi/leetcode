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
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n <= 1:
            return n

        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for j in range(n - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                candies[j] = max(candies[j + 1] + 1, candies[j])
        return sum(candies)


'''
方法一：两次遍历
思路及解法

我们可以将「相邻的孩子中，评分高的孩子必须获得更多的糖果」这句话拆分为两个规则，分别处理。
左规则：当 ratings[i - 1] < ratings[i] 时，i 号学生的糖果数量将比 i - 1 号孩子的糖果数量多。
右规则：当 ratings[i] > ratings[i + 1] 时，i 号学生的糖果数量将比 i + 1 号孩子的糖果数量多。
我们遍历该数组两次，处理出每一个学生分别满足左规则或右规则时，最少需要被分得的糖果数量。
每个人最终分得的糖果数量即为这两个数量的最大值。

具体地，以左规则为例：我们从左到右遍历该数组，假设当前遍历到位置 i，如果有 ratings[i - 1] < ratings[i] 
那么 i 号学生的糖果数量将比 i - 1号孩子的糖果数量多，我们令 left[i] = left[i - 1] + 1 即可，
否则我们令 left[i] = 1。

在实际代码中，我们先计算出左规则 left数组，在计算右规则的时候只需要用单个变量记录当前位置的右规则，同时计算答案即可。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/candy/solution/fen-fa-tang-guo-by-leetcode-solution-f01p/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [0] * n
        for i in range(n):
            if i > 0 and ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1

        right = ret = 0
        for i in range(n - 1, -1, -1):
            if i < n - 1 and ratings[i] > ratings[i + 1]:
                right += 1
            else:
                right = 1
            ret += max(left[i], right)

        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.candy([1, 0, 2]))
    print(s.candy([1, 2, 2]))
    print(s.candy([1, 2, 3, 4, 5]))
    print(s.candy([1, 1, 1, 1, 1]))
    print(s.candy([1]))
