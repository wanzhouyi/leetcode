"""
给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔2k 个字符的前 k 个字符进行反转。
如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

示例:
输入: s = "abcdefg", k = 2
输出: "bacdfeg"

提示：
该字符串只包含小写英文字母。
给定字符串的长度和 k 在 [1, 10000] 范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-string-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # 方法一，暴力解法，44ms
    def reverseStr(self, s: str, k: int) -> str:
        ls = list(s)
        left = 0
        result = []
        n = len(ls)
        while left + 2 * k < n:
            result.extend(reversed(ls[left:left + k]))
            result.extend(ls[left + k:left + 2 * k])
            left = left + 2 * k
        else:
            if n - left < k:
                result.extend(reversed(ls[left:]))
            else:
                result.extend(reversed(ls[left:left + k]))
                result.extend(ls[left + k:])
        return ''.join(result)
    # 方法二，官方题解
    def reverseStr(self, s, k):
        a = list(s)
        for i in range(0, len(a), 2 * k):
            a[i:i + k] = reversed(a[i:i + k])
        return "".join(a)



if __name__ == '__main__':
    s = Solution()
    print(s.reverseStr(s="abcdefg", k=2))
