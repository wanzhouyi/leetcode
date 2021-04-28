"""
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

示例 1：
输入: s = "leetcode"
输出: false

示例 2：
输入: s = "abc"
输出: true
限制：
0 <= len(s) <= 100
如果你不使用额外的数据结构，会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-unique-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isUnique(self, astr: str) -> bool:
        """
        36ms,python一句流，首先将字符串转换成集合，再比较集合的大小和原字符串大小是否相等，相等返回True
        """
        return True if len(set(astr)) == len(astr) else False

    def isUnique(self, astr: str) -> bool:
        """
        44ms,这种方法使用了字典，通过对出现的元素计数来判断是否有重复元素
        """
        from collections import defaultdict
        dic = defaultdict(int)
        for s in astr:
            if dic[s] > 0:
                return False
            dic[s] += 1
        return True

    def isUnique(self, astr: str) -> bool:
        """
        32ms,这种方法使用了数组，穷举字符为计数数组的索引
        """
        counter = [0] * 26
        for s in astr:
            idx = ord(s) - 97
            counter[idx] += 1
            if counter[idx] > 1:
                return False
        return True
