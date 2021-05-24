"""
给定两个整型数字 N 与 M，以及表示比特位置的 i 与 j（i <= j，且从 0 位开始计算）。
编写一种方法，使 M 对应的二进制数字插入 N 对应的二进制数字的第 i ~ j 位区域，不足之处用 0 补齐。具体插入过程如图所示。
题目保证从 i 位到 j 位足以容纳 M， 例如： M = 10011，则 i～j 区域至少可容纳 5 位。

示例1:

 输入：N = 1024(10000000000), M = 19(10011), i = 2, j = 6
 输出：N = 1100(10001001100)
示例2:

 输入： N = 0, M = 31(11111), i = 0, j = 4
 输出：N = 31(11111)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-into-bits-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        str_N = bin(N)[2:]
        str_M = bin(M)[2:]
        len_N = len(str_N)
        len_M = len(str_M)
        if len_M == j - i + 1:
            insert_str = str_M
            res = str_N[:-(j + 1)] + insert_str + str_N[len_N - i:]
            return int(res, 2)
        else:
            insert_str = '0' * (j - i + 1 - len_M) + str_M
            res = str_N[:-(j + 1)] + insert_str + str_N[len_N - i:]
            return int(res, 2)


class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        """
        特判 —— M>=N时，N对应32bits字符串长度一定<=M,替换后就是M

        三步走：

        将N的i-j为置0
        将M左移i位
        两者相或即可
        """
        if N <= M: return M
        # 构建32位字符串下标i-j为0，其他为1
        tem = "1" * (32 - j - 1) + "0" * (j - i + 1) + "1" * i
        # 将N的i-j为置0
        # 将M左移i位
        # 两者相或即可
        return (int(tem, base=2) & N) | (M << i)


if __name__ == '__main__':
    s = Solution()
    # print(s.insertBits(1024, 19, 2, 6))
    print(s.insertBits(0, 31, 0, 4))
