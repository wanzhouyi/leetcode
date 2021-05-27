"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串""。



示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。


提示：

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        lens = list(map(lambda x: len(x), strs))
        min_len = min(lens)

        for i in range(min_len):
            char = strs[0][i]
            for string in strs:
                if string[i] != char:
                    return string[:i] if string else ""
        return strs[0][:min_len]


# 以下是官解
class Solution:
    """
    方法一：横向扫描
    用 LCP(S_1 …… S_n)表示字符串 S_1……S_n的最长公共前缀。
    可以得到以下结论：
    LCP(S_1 …… S_n)=LCP(LCP(LCP(S_1,S_2),S_3),......S_n))
    基于该结论，可以得到一种查找字符串数组中的最长公共前缀的简单方法。
    依次遍历字符串数组中的每个字符串，对于每个遍历到的字符串，更新最长公共前缀，
    当遍历完所有的字符串以后，即可得到字符串数组中的最长公共前缀。
    如果在尚未遍历完所有的字符串时，最长公共前缀已经是空串，则最长公共前缀一定是空串，
    因此不需要继续遍历剩下的字符串，直接返回空串即可。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break

        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]


class Solution:
    """
    方法二：纵向扫描
    方法一是横向扫描，依次遍历每个字符串，更新最长公共前缀。另一种方法是纵向扫描。纵向扫描时，从前往后遍历所有字符串的每一列，比较相同列上的字符是否相同，如果相同则继续对下一列进行比较，如果不相同则当前列不再属于公共前缀，当前列之前的部分为最长公共前缀。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]

        return strs[0]


class Solution:
    """
    注意到LCP 的计算满足结合律，有以下结论：
    LCP(S_1 …… S_n)=LCP(LCP(S_1 …… S_k),LCP(S_k+1 …… S_n))
    其中 LCP(S_1 …… S_n)是字符串 S_1……S_n的最长公共前缀，1 < k < n1<k<n。

    基于上述结论，可以使用分治法得到字符串数组中的最长公共前缀。对于问题 LCP(S_i …… S_j)，
    可以分解成两个子问题 LCP(S_1 …… S_mid)与 LCP(S_mid …… S_j)，其中 mid=(i+j)/2。
    对两个子问题分别求解，然后对两个子问题的解计算最长公共前缀，即为原问题的解。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        def lcp(start, end):
            if start == end:
                return strs[start]

            mid = (start + end) // 2
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
            minLength = min(len(lcpLeft), len(lcpRight))
            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]

            return lcpLeft[:minLength]

        return "" if not strs else lcp(0, len(strs) - 1)
