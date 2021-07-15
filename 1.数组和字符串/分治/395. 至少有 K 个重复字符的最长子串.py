"""
给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串，要求该子串中的每一字符出现次数都不少于 k 。
返回这一子串的长度。
示例 1：
输入：s = "aaabb", k = 3
输出：3
解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。
示例 2：
输入：s = "ababbc", k = 2
输出：5
解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。

提示：

1 <= s.length <= 10^4
s 仅由小写英文字母组成
1 <= k <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # 分治和递归
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        c = min(set(s), key=s.count)
        if s.count(c) >= k:
            return s.count(c)
        return max(self.longestSubstring(t, k) for t in s.split(c))


class Solution(object):
    # 分治和递归
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


class Solution(object):
    """
    滑动窗口
    1、字符串中字符种类数 就是遍历次数max_cnt
    2、分别遍历包含1个2个..max_cnt个字符 的区间长度
    """

    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_len = 0
        max_cnt = len(set(s))
        for i in range(1, max_cnt + 1):
            once_len = self.getMaxKcharLen(s, k, i)
            max_len = max(max_len, once_len)
        return max_len

    def getMaxKcharLen(self, s, k, num):
        """
        s: 源串
        k: 次数
        num:包含num个字母
        """

        memo = {}
        cnt = 0
        max_len = 0
        left, right = 0, 0
        n = len(s)
        while right < n:
            c = s[right]
            memo[c] = memo.get(c, 0) + 1
            if memo[c] == k:
                cnt += 1

            if len(memo) == num and cnt == num:
                max_len = max(max_len, right - left + 1)

            # 缩小窗口
            while left < right and len(memo) > num:
                c = s[left]
                if memo[c] == k:
                    cnt -= 1
                memo[c] -= 1

                if memo[c] == 0:
                    del memo[c]
                left += 1
            right += 1
        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.longestSubstring("aaabb", 2))
