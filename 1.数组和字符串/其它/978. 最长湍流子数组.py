"""
当 A的子数组A[i], A[i+1], ..., A[j]满足下列条件时，我们称其为湍流子数组：

若i <= k < j，当 k为奇数时，A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
或 若i <= k < j，当 k 为偶数时，A[k] > A[k+1]，且当 k为奇数时，A[k] < A[k+1]。
也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。

返回 A 的最大湍流子数组的长度。

示例 1：

输入：[9,4,2,10,7,8,8,1,9]
输出：5
解释：(A[1] > A[2] < A[3] > A[4] < A[5])
示例 2：

输入：[4,8,12,16]
输出：2
示例 3：

输入：[100]
输出：1


提示：

1 <= A.length <= 40000
0 <= A[i] <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-turbulent-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 解法一，栈，65%
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        result = []
        n = len(arr)
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                result.append(">")
            elif arr[i] < arr[i - 1]:
                result.append("<")
            else:
                result.append("=")
        # print(result)

        stack = []
        ans = 0
        for sign in result:

            if stack and (stack[-1] == sign or sign == "="):
                temp_ans = 1
                last = stack.pop()
                while stack and stack[-1] != last:
                    last = stack.pop()
                    temp_ans += 1
                ans = max(ans, temp_ans)
            if sign != "=":
                stack.append(sign)

        temp_ans = 1
        if stack:
            last = stack.pop()
            while stack and stack[-1] != last:
                last = stack.pop()
                temp_ans += 1
            ans = max(ans, temp_ans)
        return ans + 1

    # 官方解法一，滑动窗口
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        方法一：滑动窗口
        设数组arr 的长度为 n，窗口[left,right](0≤left≤right≤n−1) 为当前的窗口，窗口内构成了一个「湍流子数组」。随后，我们要考虑下一个窗口的位置。
        根据「湍流子数组」的定义，当 0<right<n−1 时：

        如果arr[right−1]<arr[right] 且 arr[right]>arr[right+1]，则 [left,right+1] 也构成「湍流子数组」，因此需要将right 右移一个单位；
        如果arr[right−1]>arr[right] 且 arr[right]<arr[right+1]，同理，也需要将right 右移一个单位；
        否则，[right−1,right+1] 无法构成「湍流子数组」，当 left<right 时，[left,right+1] 也无法构成「湍流子数组」，因此需要将 left 移到 right，即令left=right。

        此外，我们还需要特殊考虑窗口长度为 1 (即 left 和right 相等的情况)：只要 arr[right]=arr[right+1]，就可以将right 右移一个单位；否则，left 和 right 都要同时右移。

        """
        n = len(arr)
        ans = 1
        left, right = 0, 0
        while right < n - 1:
            if left == right:
                if arr[left] == arr[right]:
                    left += 1
                right += 1
            else:
                if arr[right - 1] < arr[right] and arr[right] > arr[right + 1]:
                    right += 1
                elif arr[right - 1] > arr[right] and arr[right] < arr[right + 1]:
                    right += 1
                else:
                    left = right
            ans = max(ans, right - left + 1)
        return ans

    # 官方解法二，动态规划
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        对于本题，如果只定一个状态数组是不够的，因为我们只有区分了 i 位置是在增长还是在降低，才能判断 i + 1 位置是否能续上前面的波浪。所以，我们需要定义两个状态数组，分别表示以 i 结尾的在增长和降低的最长湍流子数组长度。

        状态的定义：
        定义 up[i] 表示以位置 i 结尾的，并且 arr[i - 1] < arr[i] 的最长湍流子数组长度。
        定义 down[i] 表示以位置 i 结尾的，并且 arr[i - 1] > arr[i] 的最长湍流子数组长度。
        up[i] 和 down[i] 初始化都是 1，因为每个数字本身都是一个最小的湍流子数组。

        状态转移方程：
        up[i] = down[i - 1] + 1，当 arr[i - 1] < arr[i]；
        down[i] = up[i - 1] + 1，当 arr[i - 1] > arr[i]；

        作者：fuxuemingzhu
        链接：https://leetcode-cn.com/problems/longest-turbulent-subarray/solution/yi-zhang-dong-tu-xiang-jie-dong-tai-gui-wrwvn/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
        N = len(arr)
        up = [1] * N
        down = [1] * N
        res = 1
        for i in range(1, N):
            if arr[i - 1] < arr[i]:
                up[i] = down[i - 1] + 1
                down[i] = 1
            elif arr[i - 1] > arr[i]:
                up[i] = 1
                down[i] = up[i - 1] + 1
            else:
                up[i] = 1
                down[i] = 1
            res = max(res, max(up[i], down[i]))
        return res
