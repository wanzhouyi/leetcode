"""
下一个数。给定一个正整数，找出与其二进制表达式中1的个数相同且大小最接近的那两个数（一个略大，一个略小）。

示例1:

 输入：num = 2（或者0b10）
 输出：[4, 1] 或者（[0b100, 0b1]）
示例2:

 输入：num = 1
 输出：[2, -1]
提示:

num的范围在[1, 2147483647]之间；
如果找不到前一个或者后一个满足条件的正数，那么输出 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/closed-number-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 这个思路不全，打叉
    def findClosedNumbers(self, num: int) -> List[int]:
        bit_num = bin(num)[2:]
        bit_num = '0' * (32 - len(bit_num)) + bit_num
        print(num, bit_num)

        idx1 = bit_num.rfind('1')
        idx2 = bit_num.rfind('0', 0, idx1)
        if idx2 == -1:
            bigger = -1
        else:
            bigger_2 = bit_num[:idx2] + '1' + bit_num[idx2 + 1:idx1] + '0' + bit_num[idx1 + 1:]
            bigger = int(bigger_2, 2)

        idx3 = bit_num.rfind('1')
        idx4 = bit_num.find('0', idx3)
        if idx4 == -1:
            lesser = -1
        else:
            lesser_2 = bit_num[:idx3] + '0' + bit_num[idx3 + 1:idx4] + '1' + bit_num[idx4 + 1:]
            lesser = int(lesser_2, 2)

        idx3 = bit_num.rfind('0')
        idx4 = bit_num.find('1', 0, idx3)
        if idx4 == -1:
            lesser = -1
        else:
            lesser_2 = bit_num[:idx4] + '0' + bit_num[idx4 + 1:idx3] + '1' + bit_num[idx3 + 1:]
            lesser = max(int(lesser_2, 2), lesser)
        return [bigger, lesser]


class Solution:
    """
    要想找一个数最近的俩数，那么就找01 和 10 这中特殊的位置，进行翻转
    找较小时，将10 变成01，并将后面所有的1都排在前面，0排在后面
    找较大时，将01变成10，后面的先0后1
    注意，较大数是可以进位的，比如10，较大的那个数是100，所以在每个二进制前面先加一个0便于应对这种情况

    2147483647这个用例过不了
    作者：wei-lan-se-de-feng-bao
    链接：https://leetcode-cn.com/problems/closed-number-lcci/solution/python3-xun-zhao-10he-01fan-zhuan-by-wei-lan-se-de/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def findClosedNumbers(self, num):
        # 较大就找'01'变成'10'
        num = str(bin(num))[2:]  # 去掉'0b'
        if not '0' in num:
            res = '10' + num[1:]
            return [int('0b' + res, 2), -1]

        num = '0' + num  # 在前面添加一个0
        temp = num[::]
        small = -1
        big = -1
        for i in range(len(temp) - 1, -1, -1):
            # print(temp)
            if temp[i:i + 2] == '10':
                t = temp[i + 2:]
                temp = temp[0:i] + '01' + '1' * t.count('1') + '0' * t.count('0')
                small = temp[::]
                break
        temp = num[::]
        # print(temp)
        for i in range(len(temp) - 1, -1, -1):
            if temp[i:i + 2] == '01':
                t = temp[i + 2:]
                temp = temp[0:i] + '10' + '0' * t.count('0') + '1' * t.count('1')
                big = temp[::]
                break
        if small != -1:
            small = int('0b' + small, 2)
        if big != -1:
            big = int('0b' + big, 2)
        return [big, small]


class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        mn, mx = 1, 2147483647

        def findLarge(n):
            # 从右开始找到第1个1
            # 然后记录1的个数ones直到再遇到0或到最高位
            # 然后将这个0变成1
            # 然后右边的位数用000...111(ones-1个1)填充
            checkMask = 1
            bits = 0
            while checkMask <= n and checkMask & n == 0:
                checkMask <<= 1
                bits += 1
            ones = 0  # 直接构造出000...111
            while checkMask <= n and checkMask & n != 0:
                ones = (ones << 1) + 1
                checkMask <<= 1
                bits += 1
            # 因为在改变的位已经将1个0转成1了, 所以这里ones要向右移动一位
            ones >>= 1
            # 将0转成1
            n |= checkMask
            # 清除右边的0
            n = (n >> bits) << bits
            # 将右边填充上ones
            n |= ones
            return n if mn <= n <= mx else -1

        def findSmall(n):
            # 从右开始找到第1个0, 记录此过程1的个数ones
            # 然后继续往左找直到再遇到1
            # 然后将这个1变成0, ones也要左移一位(也可以初始化为1)
            # 然后右边的位数用高位ones个1填充, 即构造出111...000, 可以直接基于ones构造
            # 注意如果全为1的话是无解的, 直接返回-1
            checkMask = 1
            bits = 0
            ones = 1
            while checkMask <= n and checkMask & n != 0:
                checkMask <<= 1
                bits += 1
                ones = (ones << 1) + 1
            if checkMask > n:
                # 全部是1
                return -1
            while checkMask <= n and checkMask & n == 0:
                checkMask <<= 1
                bits += 1
                ones <<= 1
            # 因为ones初始化为1, 所以ones需要右移一位
            ones >>= 1
            # 将需要改变的1变成0
            n &= ~checkMask
            # 清除右边的0
            n = (n >> bits) << bits
            # 将右边填充上ones
            n |= ones
            return n if mn <= n <= mx else -1

        return [findLarge(num), findSmall(num)]


if __name__ == '__main__':
    s = Solution()
    print(s.findClosedNumbers(num=2))  # [4, 1]
    print(s.findClosedNumbers(num=1))  # [2, -1]
    print(s.findClosedNumbers(num=3))  # [6, -1]
    print(s.findClosedNumbers(num=4))  # [8, 2]
    print(s.findClosedNumbers(num=5))
    print(s.findClosedNumbers(67))
