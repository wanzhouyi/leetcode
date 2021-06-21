"""
输入一个字符串，打印出该字符串中字符的所有排列。



你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。



示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]


限制：

1 <= s 的长度 <= 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        from itertools import permutations
        return [''.join(x) for x in (set(permutations(s)))]

    def permutation(self, s: str) -> List[str]:
        ans = set()

        def dfs(chars, path):
            if not chars:
                ans.add(path)
                return
            for i in range(len(chars)):
                dfs(chars[:i] + chars[i + 1:], path + chars[i])

        dfs(s, '')
        return list(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.permutation(s="abcc"))
    print(s.permutation(s="abc"))
    print(s.permutation(s="a"))
    print(s.permutation(s="ab"))
    print(s.permutation(s="aa"))
    print(s.permutation(s="abcdefgh"))
