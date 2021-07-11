"""
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
示例 1:
输入:
"tree"
输出:
"eert"
解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
示例 2:
输入:
"cccaaa"
输出:
"cccaaa"
解释:
'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。
示例 3:
输入:
"Aabb"
输出:
"bbAa"

解释:
此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意'A'和'a'被认为是两种不同的字符。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-characters-by-frequency
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        ct = Counter(s)
        ls = sorted(ct.items(), key=lambda x: x[1])
        ans = []
        while ls:
            key, val = ls.pop()
            ans.extend([key] * val)
        return ''.join(ans)


class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        return "".join(v for v in sorted(c.keys(), key=lambda x: -c[x]) for i in range(c[v]))


if __name__ == '__main__':
    s = Solution()
    print(s.frequencySort("tree"))
