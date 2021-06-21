"""
二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。每个 LED 代表一个 0 或 1，最低位在右侧。

例如，下面的二进制手表读取 "3:25" 。


（图源：WikiMedia - Binary clock samui moon.jpg ，许可协议：Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0) ）

给你一个整数 turnedOn ，表示当前亮着的 LED 的数量，返回二进制手表可以表示的所有可能时间。你可以 按任意顺序 返回答案。

小时不会以零开头：

例如，"01:00" 是无效的时间，正确的写法应该是 "1:00" 。
分钟必须由两位数组成，可能会以零开头：

例如，"10:2" 是无效的时间，正确的写法应该是 "10:02" 。


示例 1：

输入：turnedOn = 1
输出：["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
示例 2：

输入：turnedOn = 9
输出：[]


提示：

0 <= turnedOn <= 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-watch
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
from itertools import combinations
from functools import lru_cache


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        h_enum = [1, 2, 4, 8]
        m_enum = [1, 2, 4, 8, 16, 32]

        @lru_cache(None)
        def hour(h):
            return list(filter(lambda a: a < 12, map(lambda x: sum(x), combinations(h_enum, h))))

        @lru_cache(None)
        def minite(m):
            return list(filter(lambda a: a < 60, map(lambda x: sum(x), combinations(m_enum, m))))

        ans = []
        for i in range(turnedOn + 1):
            h = hour(i)
            m = minite(turnedOn - i)
            for x in h:
                for y in m:
                    ans.append(str(x) + ':' + ('0' if y < 10 else '') + str(y))
        return ans


# 以下是官解
class Solution:
    """
    方法一：枚举时分
    由题意可知，小时由 4 个比特表示，分钟由 6 个比特表示，比特位值为 0 表示灯灭，为 1 表示灯亮。
    我们可以枚举小时的所有可能值 [0,11]，以及分钟的所有可能值[0,59]，并计算二者的二进制中 1 的个数之和，若为turnedOn，则将其加入到答案中。
    """

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = list()
        for h in range(12):
            for m in range(60):
                if bin(h).count("1") + bin(m).count("1") == turnedOn:
                    ans.append(f"{h}:{m:02d}")
        return ans


class Solution:
    """
    另一种枚举方法是枚举所有 2^10=1024种灯的开闭组合，即用一个二进制数表示灯的开闭，其高 4 位为小时，低 6 位为分钟。
    若小时和分钟的值均在合法范围内，且二进制中 1 的个数为turnedOn，则将其加入到答案中。

    """

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = list()
        for i in range(1024):
            h, m = i >> 6, i & 0x3f  # 用位运算取出高 4 位和低 6 位
            if h < 12 and m < 60 and bin(i).count("1") == turnedOn:
                ans.append(f"{h}:{m:02d}")
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.readBinaryWatch(1))
    print(s.readBinaryWatch(2))
    print(s.readBinaryWatch(3))
    print(s.readBinaryWatch(4))
    print(s.readBinaryWatch(5))
    print(s.readBinaryWatch(9))
