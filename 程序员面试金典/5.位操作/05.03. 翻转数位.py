"""
给定一个32位整数 num，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。

示例 1：

输入: num = 1775(110111011112)
输出: 8
示例 2：

输入: num = 7(01112)
输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-bits-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def reverseBits(self, num: int) -> int:

        if num > 0:
            bit2 = bin(num)[2:]
            bit2 = '0' * (32 - len(bit2)) + bit2
        else:
            fan = ~num
            bit2 = bin(fan)

        left = 0
        ans = 0
        counter0 = 0
        for right in range(len(bit2)):
            if bit2[right] == '1':
                ans = max(ans, right - left + 1)
            else:
                counter0 += 1
                if counter0 <= 1:
                    ans = max(ans, right - left + 1)
                else:
                    while counter0 > 1:
                        if bit2[left] == '0':
                            counter0 -= 1
                        left += 1

        return ans


class Solution:
    def reverseBits(self, num: int) -> int:
        pre, cur = 0, 0
        res = 1
        for i in range(32):
            if num & (1 << i):
                cur += 1
            else:
                res = max(res, pre + cur)
                pre = cur + 1
                cur = 0
        res = max(res, pre + cur)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(num=1775))  # 8
    print(s.reverseBits(num=7))  # 4
