"""
给你一个字符串 s，找到 s 中最长的回文子串。
示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"

示例 3：
输入：s = "a"
输出："a"

示例 4：
输入：s = "ac"
输出："a"

提示：
1 <= s.length <= 1000
s 仅由数字和英文字母（大写和/或小写）组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    """
    先暴力一把，用特殊字符消除奇偶性
    abc-->#a#b#c#
    abcd-->#a#b#c#d#
    过，60%
    """

    def longestPalindrome(self, s: str) -> str:
        s1 = '#' + '#'.join(s) + '#'
        # print(s1)
        n = len(s1)
        ans = ''
        for i in range(n):
            left, right = i, i
            while left > 0 and right < n and s1[left] == s1[right]:
                left -= 1
                right += 1
            ans = max(ans, s1[left + 1:right], key=len)
        return ans.replace('#', '')


# 其它解法

class Solution:
    """
    方法一：动态规划
    思路与算法
    对于一个子串而言，如果它是回文串，并且长度大于 2，那么将它首尾的两个字母去除之后，它仍然是个回文串。
    例如对于字符串 “ababa”，如果我们已经知道“bab” 是回文串，那么“ababa” 一定是回文串，
    这是因为它的首尾两个字母都是“a”。

    根据这样的思路，我们就可以用动态规划的方法解决本题。
    我们用 P(i,j)表示字符串 s 的第 i 到 j 个字母组成的串（下文表示成 s[i:j]）是否为回文串：

    P(i,j)={
        true, # 如果子串 S_i…S_j是回文串
        false # 其它情况
    }

    这里的「其它情况」包含两种可能性：
        s[i, j]本身不是一个回文串；
        i > j，此时 s[i, j] 本身不合法。

    那么我们就可以写出动态规划的状态转移方程：
    P(i,j)=P(i+1,j−1)∧(S_i == S_j)
    也就是说，只有 s[i+1:j-1] 是回文串，并且 s 的第 i 和 j 个字母相同时，s[i:j] 才会是回文串。

    上文的所有讨论是建立在子串长度大于 2 的前提之上的，我们还需要考虑动态规划中的边界条件，即子串的长度为 1 或 2。
    对于长度为 1 的子串，它显然是个回文串；对于长度为 2 的子串，只要它的两个字母相同，它就是一个回文串。
    因此我们就可以写出动态规划的边界条件：

    {
        P(i,i)=true
        P(i,i+1)=(S_i==S_(i+1) )
    }

    根据这个思路，我们就可以完成动态规划了，最终的答案即为所有P(i,j)=true 中 j-i+1（即子串长度）的最大值。
    注意：在状态转移方程中，我们是从长度较短的字符串向长度较长的字符串进行转移的，因此一定要注意动态规划的循环顺序。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]


class Solution:
    """
    方法二：中心扩展算法
    思路与算法

    我们仔细观察一下方法一中的状态转移方程：
    找出其中的状态转移链：    P(i,j)←P(i+1,j−1)←P(i+2,j−2)←⋯←某一边界情况
    可以发现，所有的状态在转移的时候的可能性都是唯一的。
    也就是说，我们可以从每一种边界情况开始「扩展」，也可以得出所有的状态对应的答案。

    边界情况即为子串长度为 1 或 2 的情况。我们枚举每一种边界情况，并从对应的子串开始不断地向两边扩展。
    如果两边的字母相同，我们就可以继续扩展，例如从 P(i+1,j-1)扩展到 P(i,j)；
    如果两边的字母不同，我们就可以停止扩展，因为在这之后的子串都不能是回文串了。

    聪明的读者此时应该可以发现，「边界情况」对应的子串实际上就是我们「扩展」出的回文串的「回文中心」。
    方法二的本质即为：我们枚举所有的「回文中心」并尝试「扩展」，直到无法扩展为止，
    此时的回文串长度即为此「回文中心」下的最长回文串长度。我们对所有的长度求出最大值，即可得到最终的答案。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]


class Solution:
    """
    方法三：Manacher 算法
    还有一个复杂度为 O(n) 的 Manacher 算法。然而本算法十分复杂，一般不作为面试内容。
    这里给出，仅供有兴趣的同学挑战自己。
    为了表述方便，我们定义一个新概念臂长，表示中心扩展算法向外扩展的长度。
    如果一个位置的最大回文字符串长度为 2 * length + 1 ，其臂长为 length。
    下面的讨论只涉及长度为奇数的回文字符串。长度为偶数的回文字符串我们将会在最后与长度为奇数的情况统一起来。
    思路与算法
    在中心扩展算法的过程中，我们能够得出每个位置的臂长。那么当我们要得出以下一个位置 i 的臂长时，能不能利用之前得到的信息呢？
    答案是肯定的。具体来说，如果位置 j 的臂长为 length，并且有 j + length > i，如下图所示：

    当在位置 i 开始进行中心拓展时，我们可以先找到 i 关于 j 的对称点 2 * j - i。
    那么如果点 2 * j - i 的臂长等于 n，我们就可以知道，点 i 的臂长至少为 min(j + length - i, n)。
    那么我们就可以直接跳过 i 到 i + min(j + length - i, n) 这部分，从 i + min(j + length - i, n) + 1 开始拓展。

    我们只需要在中心扩展法的过程中记录右臂在最右边的回文字符串，将其中心作为 j，在计算过程中就能最大限度地避免重复计算。

    那么现在还有一个问题：如何处理长度为偶数的回文字符串呢？
    我们可以通过一个特别的操作将奇偶数的情况统一起来：我们向字符串的头尾以及每两个字符中间添加一个特殊字符 #，
    比如字符串 aaba 处理后会变成 #a#a#b#a#。那么原先长度为偶数的回文字符串 aa 会变成长度为奇数的回文字符串 #a#a#，
    而长度为奇数的回文字符串 aba 会变成长度仍然为奇数的回文字符串 #a#b#a#，我们就不需要再考虑长度为偶数的回文字符串了。
    注意这里的特殊字符不需要是没有出现过的字母，我们可以使用任何一个字符来作为这个特殊字符。这是因为，当我们只考虑长度为奇数的回文字符串时，每次我们比较的两个字符奇偶性一定是相同的，所以原来字符串中的字符不会与插入的特殊字符互相比较，不会因此产生问题。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def longestPalindrome(self, s: str) -> str:
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start + 1:end + 1:2]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome(s="babad"))
    print(s.longestPalindrome(s="cbbd"))
    print(s.longestPalindrome(s="a"))
    print(s.longestPalindrome(s="ac"))
