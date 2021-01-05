"""
实现int sqrt(int x)函数。
计算并返回x的平方根，其中x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
输入: 4
输出: 2

示例 2:
输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
    由于返回类型是整数，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # 方法一，使用系统函数，44ms，76%
    def mySqrt(self, x: int) -> int:
        import math
        return math.floor(math.sqrt(x))

    # 方法二，二分查找（左闭右开），52ms，46%
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        left, right = 0, x + 1
        while left < right:
            mid = left + (right - left) // 2
            mid2 = mid ** 2
            if mid2 > x:
                right = mid
            elif mid2 < x:
                left = mid + 1
            else:
                return mid
        return left - 1

    # 方法三，二分查找（左闭右闭），48ms，61%
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2
            mid2 = mid ** 2
            if mid2 > x:
                right = mid - 1
            elif mid2 < x:
                left = mid + 1
            elif mid2 == x:
                return mid
        return left - 1


if __name__ == '__main__':
    s = Solution()
    print([(i, s.mySqrt(i)) for i in range(18)])
