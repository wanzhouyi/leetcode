"""
有一个正整数数组arr，现给你一个对应的查询数组queries，其中queries[i] = [Li,Ri]。
对于每个查询i，请你计算从Li到Ri的XOR值（即arr[Li] xor arr[Li+1] xor ... xor arr[Ri]）作为本次查询的结果。
并返回一个包含给定查询queries所有结果的数组。

示例 1：
输入：arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
输出：[2,7,14,8] 
解释：
数组中元素的二进制表示形式是：
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
查询的 XOR 值为：
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8

示例 2：
输入：arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
输出：[8,0,4,4]

提示：

1 <= arr.length <= 3 *10^4
1 <= arr[i] <= 10^9
1 <= queries.length <= 3 * 10^4
queries[i].length == 2
0 <= queries[i][0] <= queries[i][1] < arr.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xor-queries-of-a-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        """暴力解法，会超时"""
        ans = []
        for ln, rn in queries:
            temp = arr[ln]
            for num in range(ln + 1, rn + 1):
                temp ^= arr[num]
            ans.append(temp)
        return ans

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        """应用了前缀异或的方法"""
        pre_arr = [0]
        for num in arr:
            pre_arr.append(pre_arr[-1] ^ num)

        ans = []
        for ln, rn in queries:
            pre_ln = pre_arr[ln]
            pre_rn = pre_arr[rn + 1]
            ans.append(pre_ln ^ pre_rn)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.xorQueries(arr=[1, 3, 4, 8], queries=[[0, 1], [1, 2], [0, 3], [3, 3]]))  # [2, 7, 14, 8]
    print(s.xorQueries(arr=[4, 8, 2, 10], queries=[[2, 3], [1, 3], [0, 0], [0, 3]]))  # [8, 0, 4, 4]
