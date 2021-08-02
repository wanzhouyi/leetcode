"""给你一个数组target，包含若干 互不相同的整数，以及另一个整数数组arr，arr可能 包含重复元素。 每一次操作中，你可以在 arr的任意位置插入任一整数。比方说，如果arr = [
1,4,1,2]，那么你可以在中间添加 3得到[1,4,3,1,2]。你可以在数组最开始或最后面添加整数。 请你返回 最少操作次数，使得target成为arr的一个子序列。 一个数组的
子序列指的是删除原数组的某些元素（可能一个元素都不删除），同时不改变其余元素的相对顺序得到的数组。比方说，[2,7,4]是[4,2,3,7,2,1,4]的子序列（加粗元素），但[2,4,
2]不是子序列。

示例 1：
输入：target = [5,1,3], arr = [9,4,2,3,4]
输出：2
解释：你可以添加 5 和 1 ，使得 arr 变为 [5,9,4,1,2,3,4] ，target 为 arr 的子序列。
示例 2：
输入：target = [6,4,8,1,3,2], arr = [4,7,6,2,3,8,6,1]
输出：3

提示：

1 <= target.length, arr.length <= 105
1 <= target[i], arr[i] <= 109
target不包含任何重复元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-operations-to-make-a-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import bisect
from typing import List


class Solution:
    """
    方法一：贪心 + 二分查找
    记数组 target 的长度为 nn，数组arr 的长度为 m。
    根据题意，target 和arr 这两个数组的公共子序列越长，需要添加的元素个数也就越少。
    因此最少添加的元素个数为 n 减去两数组的最长公共子序列的长度。

    求最长公共子序列是一个经典问题，读者可参考「1143. 最长公共子序列的官方题解」。
    但是，这一做法的时间复杂度是 O(nm) 的，在本题的数据范围下无法承受，我们需要改变思路。

    由于 target 的元素互不相同，我们可以用一个哈希表记录 target 的每个元素所处的下标，并将 arr 中的元素映射到下标上，
    对于不存在于target 中的元素，由于其必然不会在最长公共子序列中，可将其忽略。

    我们使用示例 2 来说明，将 arr 中的元素转换成该元素在target 中的下标（去掉不在 target 中的元素 7），可以得到一个新数组

    arr' = [1,0,5,4,2,0,3]
    若将 target 也做上述转换，这相当于将每个元素变为其下标，得

    target′ =[0,1,2,3,4,5]
    则求原数组的最长公共子序列等价于求上述转换后的两数组的最长公共子序列。
    注意到 target′是严格单调递增的，因此 arr′ 在最长公共子序列中的部分也必须是严格单调递增的，
    因此问题可进一步地转换成求 arr′ 的最长递增子序列的长度。
    这也是一个经典问题，读者可以参考「300. 最长递增子序列的官方题解」，使用贪心和二分查找的方法得到最长递增子序列的长度。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/minimum-operations-to-make-a-subsequence/solution/de-dao-zi-xu-lie-de-zui-shao-cao-zuo-ci-hefgl/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def minOperations(self, target: List[int], arr: List[int]) -> int:
        n = len(target)
        pos = {}
        for i, t in enumerate(target):
            pos[t] = i

        d = []
        for val in arr:
            if val in pos:
                idx = pos[val]
                site = bisect.bisect_left(d, idx)
                if site < len(d):
                    d[site] = idx
                else:
                    d.append(idx)

        return n - len(d)


if __name__ == '__main__':
    s = Solution()
    print(s.minOperations(target=[6, 4, 8, 1, 3, 2], arr=[4, 7, 6, 2, 3, 8, 6, 1]))
