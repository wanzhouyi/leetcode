"""
给你一个字符串s，以及该字符串中的一些「索引对」数组pairs，其中pairs[i] =[a, b]表示字符串中的两个索引（编号从 0 开始）。
你可以 任意多次交换 在pairs中任意一对索引处的字符。
返回在经过若干次交换后，s可以变成的按字典序最小的字符串。

示例 1:
输入：s = "dcab", pairs = [[0,3],[1,2]]
输出："bacd"
解释： 
交换 s[0] 和 s[3], s = "bcad"
交换 s[1] 和 s[2], s = "bacd"

示例 2：
输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
输出："abcd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[0] 和 s[2], s = "acbd"
交换 s[1] 和 s[2], s = "abcd"

示例 3：
输入：s = "cba", pairs = [[0,1],[1,2]]
输出："abc"
解释：
交换 s[0] 和 s[1], s = "bca"
交换 s[1] 和 s[2], s = "bac"
交换 s[0] 和 s[1], s = "abc"

提示：

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] <s.length
s中只含有小写英文字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-string-with-swaps
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        from collections import defaultdict
        n = len(s)
        ls = [i for i in range(n)]
        size = [1] * n

        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return
            if size[a] < size[b]:
                root_a, root_b = root_b, root_a
            size[a] += size[b]
            ls[root_a] = root_b

        def find(x):
            while x != ls[x]:
                x = ls[x]
            return x

        for pair in pairs:
            union(pair[0], pair[1])

        mp = defaultdict(list)
        for idx, char in enumerate(s):
            mp[find(idx)].append(char)

        for mp_val in mp.values():
            mp_val.sort(reverse=True)

        result = []
        for i in range(n):
            x = find(i)
            result.append(mp[x][-1])
            mp[x].pop()
        print(result)
        return ''.join(result)


if __name__ == '__main__':
    s = Solution()
    print(s.smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2]]))
    print(s.smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2], [0, 2]]))
    print(s.smallestStringWithSwaps(s="cba", pairs=[[0, 1], [1, 2]]))
