"""
给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。



示例 1：

输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
示例 2：

输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2 。


提示：

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i]仅由'0' 和'1' 组成
1 <= m, n <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ones-and-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
from functools import lru_cache


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counter = 0
        length = len(strs)

        @lru_cache(None)
        def dp(idx: int, x: int, y: int):
            # print(idx,x,y)
            nonlocal counter
            counter += 1
            if idx > length - 1:
                return 0

            ln = len(strs[idx])
            ct0 = strs[idx].count('0')
            ct1 = ln - ct0

            # 不选
            buxuan = dp(idx + 1, x, y)

            if x + ct0 <= m and y + ct1 <= n:
                # 选
                xuan = 1 + dp(idx + 1, x + ct0, y + ct1)
                return max(xuan, buxuan)

            return buxuan

        rst = dp(0, 0, 0)
        print(counter)
        return rst


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3))
    print(s.findMaxForm(strs=["10", "0", "1"], m=1, n=1))
    print(s.findMaxForm(
        ["101", "110", "0", "0", "0", "0001", "1010", "01", "10110", "0011", "0", "10", "11", "110",
         "1", "10", "0", "1", "00", "1", "0", "010", "1", "000", "0", "101", "0", "11", "1",
         "01111", "110000", "1", "01"]
        , 47
        , 88))
