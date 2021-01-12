"""
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
给出两个整数 x 和 y，计算它们之间的汉明距离。
注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hamming-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # 方法一，异或，40 ms，57.16%
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')

    # 方法二，异或+移位，32 ms，92.56%
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        ans = 0
        while diff:
            ans += (diff & 1)
            diff = diff >> 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(x=1, y=4))
