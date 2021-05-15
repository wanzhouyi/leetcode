"""
罗马数字包含以下七种字符:I，V，X，L，C，D和M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做II，即为两个并列的 1。12 写做XII，即为X+II。 27 写做XXVII, 即为XX+V+II。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做IIII，而是IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为IX。这个特殊的规则只适用于以下六种情况：

I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
C可以放在D(500) 和M(1000) 的左边，来表示400 和900。
给定一个罗马数字，将其转换成整数。输入确保在 1到 3999 的范围内。



示例1:

输入:"III"
输出: 3
示例2:

输入:"IV"
输出: 4
示例3:

输入:"IX"
输出: 9
示例4:

输入:"LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
示例5:

输入:"MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.


提示：

1 <= s.length <= 15
s 仅含字符 ('I', 'V', 'X', 'L', 'C', 'D', 'M')
题目数据保证 s 是一个有效的罗马数字，且表示整数在范围 [1, 3999] 内
题目所给测试用例皆符合罗马数字书写规则，不会出现跨位等情况。
IL 和 IM 这样的例子并不符合题目要求，49 应该写作 XLIX，999 应该写作 CMXCIX 。
关于罗马数字的详尽书写规则，可以参考 罗马数字 - Mathematics 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/roman-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        """暴力解法"""
        ans = 0
        last_char = None
        for idx, char in enumerate(s):
            if char == 'M':
                if last_char == 'C':
                    ans -= 100
                    ans += 900
                else:
                    ans += 1000
            elif char == 'D':
                if last_char == 'C':
                    ans -= 100
                    ans += 400
                else:
                    ans += 500
            elif char == 'C':
                if last_char == 'X':
                    ans -= 10
                    ans += 90
                else:
                    ans += 100
            elif char == 'L':
                if last_char == 'X':
                    ans -= 10
                    ans += 40
                else:
                    ans += 50
            elif char == 'X':
                if last_char == 'I':
                    ans -= 1
                    ans += 9
                else:
                    ans += 10
            elif char == 'V':
                if last_char == 'I':
                    ans -= 1
                    ans += 4
                else:
                    ans += 5
            elif char == 'I':
                ans += 1

            last_char = char
        return ans


class Solution:
    """官解"""
    SYMBOL_VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i, ch in enumerate(s):
            value = Solution.SYMBOL_VALUES[ch]
            if i < n - 1 and value < Solution.SYMBOL_VALUES[s[i + 1]]:
                ans -= value
            else:
                ans += value
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("III"))
    print(s.romanToInt("IV"))
    print(s.romanToInt("IX"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV"))
