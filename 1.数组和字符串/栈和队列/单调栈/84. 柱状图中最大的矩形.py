"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为[2,1,5,6,2,3]。
图中阴影部分为所能勾勒出的最大矩形面积，其面积为10个单位。
示例:

输入: [2,1,5,6,2,3]
输出: 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List



class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/bao-li-jie-fa-zhan-by-liweiwei1419/
        """
        size = len(heights)
        res = 0

        stack = []

        for i in range(size):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]

                while len(stack) > 0 and cur_height == heights[stack[-1]]:
                    stack.pop()

                if len(stack) > 0:
                    cur_width = i - stack[-1] - 1
                else:
                    cur_width = i

                res = max(res, cur_height * cur_width)
            stack.append(i)

        while len(stack) > 0 is not None:
            cur_height = heights[stack.pop()]
            while len(stack) > 0 and cur_height == heights[stack[-1]]:
                stack.pop()

            if len(stack) > 0:
                cur_width = size - stack[-1] - 1
            else:
                cur_width = size
            res = max(res, cur_height * cur_width)

        return res

    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        哨兵
        """
        size = len(heights)
        res = 0
        heights = [0] + heights + [0]
        # 先放入哨兵结点，在循环中就不用做非空判断
        stack = [0]
        size += 2

        for i in range(1, size):
            while heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                res = max(res, cur_height * cur_width)
            stack.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    # print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # 10
    # print(s.largestRectangleArea([1] * 100))  # 100
    # print(s.largestRectangleArea([]))  # 0
    # print(s.largestRectangleArea([1, 2, 3, 4, 5, 6, 7, 8]))  # 20
    # print(s.largestRectangleArea([8, 7, 6, 5, 4, 3, 2, 1]))  # 20
    # print(s.largestRectangleArea([2]))
    # print(s.largestRectangleArea([2, 2, 1, 1, 2, 2, 1, 1, 1]))  # 9
    # print(s.largestRectangleArea([4, 0, 2, 1, 2, 3, 4, 2, 1]))  # 8
    # print(s.largestRectangleArea([2, 8, 0, 4, 8, 5, 7, 9, 10, 10]))  # 28
    # print(s.largestRectangleArea([2, 1, 2]))
    print(s.largestRectangleArea([4, 2, 0, 3, 2, 5]))  # 6
    # import random as r
    # arr = [r.randint(0, 10) for i in range(10)]
    # print(arr, s.largestRectangleArea(arr))
