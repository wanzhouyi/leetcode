"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。
如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。

示例 1：
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"

示例 2：
输入：s = "a", t = "a"
输出："a"

提示：

1 <= s.length, t.length <= 105
s 和 t 由英文字母组成

进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter, defaultdict
        ctt = Counter(t)
        cts = defaultdict(int)
        left = 0
        ans = ""
        ans_len = float('inf')
        for right, char in enumerate(s):
            cts[char] += 1
            while all(map(lambda x: ctt[x] <= cts[x], ctt.keys())):
                if right - left < ans_len:
                    ans_len = right - left
                    ans = s[left:right + 1]
                cts[s[left]] -= 1
                left += 1
        return ans

    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt = len(t)
        i = 0
        res = (0, float('inf'))
        for j, c in enumerate(s):
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:  # 步骤一：滑动窗口包含了所有T元素
                while True:  # 步骤二：增加i，排除多余元素
                    c = s[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if j - i < res[1] - res[0]:  # 记录结果
                    res = (i, j)
                need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt += 1
                i += 1
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]  # 如果res始终没被更新过，代表无满足条件的结果


if __name__ == '__main__':
    s = Solution()
    print(s.minWindow(s="ADOBECODEBANC", t="ABC"))
    print(s.minWindow(s="a", t="a"))
    print(s.minWindow(s='', t=''))
    print(s.minWindow(s='', t='a'))
    print(s.minWindow(s='aaaaa', t='a'))
