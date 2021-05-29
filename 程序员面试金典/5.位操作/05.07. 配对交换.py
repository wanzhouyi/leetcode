"""
配对交换。编写程序，交换某个整数的奇数位和偶数位，尽量使用较少的指令（也就是说，位0与位1交换，位2与位3交换，以此类推）。

示例1:

 输入：num = 2（或者0b10）
 输出 1 (或者 0b01)
示例2:

 输入：num = 3
 输出：3
提示:

num的范围在[0, 2^30 - 1]之间，不会发生整数溢出。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/exchange-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def exchangeBits(self, num: int) -> int:
        bit_list = list(bin(num)[2:])
        bit_list = ['0'] * (30 - len(bit_list)) + bit_list
        for i in range(0, len(bit_list) - 1, 2):
            bit_list[i], bit_list[i + 1] = bit_list[i + 1], bit_list[i]
        return int(''.join(bit_list), 2)


"""
int -> 32位

奇数位全1 -> 0101.... 表示为 0x55555555

偶数位全1 -> 1010.... 表示为 0xaaaaaaaa

ans = (提取奇数位 << 1) + (提取偶数位 >> 1)
"""


class Solution:
    """
    0x55555555 首先0x表示十六进制，十六进制5转换为二进制为0101也就是可以表示为0b01010101……
    0xaaaaaaaa 十六进制a转换二进制为1010，同上
    之所以选用8位十六进制是因为，题意num小于2的30次方-1，需要至少30位二进制来 与（&） 运算
    将num与以上两个十六进制字符 与 运算，与 的逻辑是 1 1 为 1，0 0 为 0 ，1 0 为 0，0 1 为0，
    所以0x555…… 与（&） num,奇数位全为0，偶数位依据num而变，同理0xaaaa 与 num，偶数位全为0，奇数依据num而变
    因为要将奇数位与偶数位互换，所以奇数位右移一位，偶数位左移一位

    <<表示左移 >>表示右移
    最后进行或运算，有1为1，都0为0，即是结果

    作者：wanghai_nihao
    链接：https://leetcode-cn.com/problems/exchange-lcci/solution/wei-yun-suan-by-wanghai_nihao-2ybo/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def exchangeBits(self, num: int) -> int:
        return (((num & 0x55555555) << 1) | ((num & 0xaaaaaaaa) >> 1))


if __name__ == '__main__':
    s = Solution()
    print(s.exchangeBits(0))  # 0
    print(s.exchangeBits(1))  # 2
    print(s.exchangeBits(2))  # 1
    print(s.exchangeBits(3))  # 3
    print(s.exchangeBits(4))  # 2
