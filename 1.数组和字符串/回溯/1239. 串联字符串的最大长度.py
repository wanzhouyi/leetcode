"""
给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。
请返回所有可行解 s 中最长长度。

示例 1：

输入：arr = ["un","iq","ue"]
输出：4
解释：所有可能的串联组合是 "","un","iq","ue","uniq" 和 "ique"，最大长度为 4。
示例 2：

输入：arr = ["cha","r","act","ers"]
输出：6
解释：可能的解答有 "chaers" 和 "acters"。
示例 3：

输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
输出：26

提示：

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i]中只含有小写英文字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        """
        隐含的测试用例：一个单词内也可能是重复的
        """

        def dp(strs: list, set_join: set):
            if not strs:
                return len(set_join)

            # 不选
            buxuan = dp(strs[1:], set_join)
            # 能不能选的标志
            if len(strs[0]) == len(set(strs[0])) and len(set_join.intersection(set(strs[0]))) == 0:
                # 能选且选
                xuan = dp(strs[1:], set_join.union(set(strs[0])))
                return max(xuan, buxuan)
            return buxuan

        return dp(arr, set())


# 官解及解释
class Solution:
    """
    方法一：回溯 + 位运算
    我们需要计算可行解的长度，至于可行解具体是什么，以及可行解中各个字符的顺序我们是不用考虑的。
    因此构成可行解的每个字符串均可以视作一个字符集合，且集合不含重复元素。
    
    由于构成可行解的字符串仅包含小写字母，且无重复元素，我们可以用一个二进制数来表示该字符串的字符集合，
    二进制的第 i 位为 1 表示字符集合中含有第 i 个小写字母，为 0表示字符集合中不含有第 i 个小写字母。
    
    由于包含重复字母的字符串无法参与构成可行解，因此遍历 arr，从中筛选出无重复字母的字符串，将其对应二进制数加入一数组，记作masks。
    
    接下来，使用回溯法来解决本问题：
    
    我们用 backtrack(pos,mask) 表示递归的函数，其中pos 表示我们当前递归到了数组 masks 中的第 pos 个数，
    mask 表示当前连接得到的字符串对应二进制数为mask；
    
    对于第pos 个数，我们有两种方法：选或者不选。
    如果mask 和 masks[pos] 无公共元素，则可以选这个数，此时我们调用backtrack(pos+1,mask∣masks[pos]) 进行递归。
    如果我们不选这个数，那么我们调用backtrack(pos+1,mask) 进行递归。
    
    记masks 的长度为 n，当pos=n 时，计算 mask 中 1 的个数，即为可行解的长度，用其更新可行解的最长长度。
    
    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/solution/chuan-lian-zi-fu-chuan-de-zui-da-chang-d-g6gk/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def maxLength(self, arr: List[str]) -> int:
        masks = list()
        for s in arr:
            mask = 0
            for ch in s:
                idx = ord(ch) - ord("a")
                if ((mask >> idx) & 1):  # // 若 mask 已有 ch，则说明 s 含有重复字母，无法构成可行解
                    mask = 0
                    break
                mask |= 1 << idx  # 将 ch 加入 mask 中
            if mask > 0:
                masks.append(mask)

        ans = 0

        def backtrack(pos: int, mask: int) -> None:
            if pos == len(masks):
                nonlocal ans
                ans = max(ans, bin(mask).count("1"))
                return

            if (mask & masks[pos]) == 0:  # mask 和 masks[pos] 无公共元素
                backtrack(pos + 1, mask | masks[pos])
            backtrack(pos + 1, mask)

        backtrack(0, 0)
        return ans


class Solution:
    def maxLength(self, arr):
        result = 0
        temp = []

        # 检查是否满足字符唯一的条件
        def can_add(current, temp):
            concat_str = ''.join(temp)
            for c in current:
                if c in concat_str:
                    return False
            return True

        # 检查字符串本身有没有重复的字符
        def is_distinct(current):
            return len(set(current)) == len(current)

        def backtrace(start, temp, arr):

            nonlocal result
            result = max(result, len(''.join(temp)))

            for i in range(start, len(arr)):

                # 这里可以控制谁要加进来, 谁可以继续回溯和pop
                if can_add(arr[i], temp) and is_distinct(arr[i]):
                    temp.append(arr[i])
                    backtrace(i + 1, temp, arr)
                    temp.pop(-1)

        backtrace(0, temp, arr)

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.maxLength(arr=["un", "iq", "ue"]))
