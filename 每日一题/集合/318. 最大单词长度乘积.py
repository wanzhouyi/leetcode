"""
给定一个字符串数组words，找到length(word[i]) * length(word[j])的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。



示例1:

输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
输出: 16 
解释: 这两个单词为 "abcw", "xtfn"。
示例 2:

输入: ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4 
解释: 这两个单词为 "ab", "cd"。
示例 3:

输入: ["a","aa","aaa","aaaa"]
输出: 0 
解释: 不存在这样的两个单词。


提示：

2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i]仅包含小写字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-of-word-lengths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        words2 = list(map(set, words))
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if len(words2[i].intersection(words2[j])) == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans
