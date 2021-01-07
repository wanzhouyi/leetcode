"""
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数n。
能否在不打破种植规则的情况下种入n朵花？能则返回True，不能则返回False。

示例 1:
输入: flowerbed = [1,0,0,0,1], n = 1
输出: True

示例 2:
输入: flowerbed = [1,0,0,0,1], n = 2
输出: False

注意:
数组内已种好的花不会违反种植规则。
输入的数组长度范围为 [1, 20000]。
n 是非负整数，且不会超过输入数组的大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/can-place-flowers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，暴力解法，60ms
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        if m == 1 and flowerbed[0] == 0:
            return n - 1 <= 0
        for i in range(m):
            if i == 0 and flowerbed[0] == 0 and i + 1 < m and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
            elif i == m - 1 and flowerbed[m - 1] == 0 and i - 1 >= 0 and flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                n -= 1
            elif 0 < i < m - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False

    # 方法二，哨兵，60ms
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        m = len(flowerbed)
        for i in range(1, m - 1):
            if 0 < i < m - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
                if n <= 0:
                    return True
        return n == 0


if __name__ == '__main__':
    s = Solution()
    print(s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1))
    print(s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))
    # n是非负整数，触发用例n=0
    print(s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=0))
    # n不会超过输入数组的大小，触发用例n=len(flowerbed)
    print(s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=5))
    # 输入的数组长度范围为 [1, 20000]
    print(s.canPlaceFlowers(flowerbed=[1], n=0))
    print(s.canPlaceFlowers(flowerbed=[1], n=1))
    print(s.canPlaceFlowers(flowerbed=[0], n=0))
    # 特别判定
    print(s.canPlaceFlowers(flowerbed=[0], n=1))
