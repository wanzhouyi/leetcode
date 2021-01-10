"""
给定一个整数，将其转化为7进制，并以字符串形式输出。

示例 1:
输入: 100
输出: "202"

示例 2:
输入: -7
输出: "-10"

注意: 输入范围是[-1e7, 1e7] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/base-7
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # 方法一，模拟，44ms，33.5%
    def convertToBase7(self, num: int) -> str:
        ans = []
        positive = True
        if num < 0:
            positive = False
            num = abs(num)
        while num >= 7:
            ans.append(str(num % 7))
            num //= 7
        ans.append(str(num))
        return ('' if positive else '-') + ''.join(ans[::-1])


if __name__ == '__main__':
    s = Solution()
    print(s.convertToBase7(100))
    print(s.convertToBase7(7))
    print(s.convertToBase7(-7))
    print(s.convertToBase7(10 ** 7))
    print(s.convertToBase7(-10 ** 7))
