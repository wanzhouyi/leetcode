"""
给你一个整数数组 nums ，数组中共有 n 个整数。132 模式的子序列 由三个整数 nums[i]、nums[j] 和 nums[k] 组成，
并同时满足：i < j < k 和 nums[i] < nums[k] < nums[j] 。
如果 nums 中存在 132 模式的子序列 ，返回 true ；否则，返回 false 。

进阶：很容易想到时间复杂度为 O(n^2) 的解决方案，你可以设计一个时间复杂度为 O(n logn) 或 O(n) 的解决方案吗？

示例 1：
输入：nums = [1,2,3,4]
输出：false
解释：序列中不存在 132 模式的子序列。

示例 2：
输入：nums = [3,1,4,2]
输出：true
解释：序列中有 1 个 132 模式的子序列： [1, 4, 2] 。

示例 3：
输入：nums = [-1,3,2,0]
输出：true
解释：序列中有 3 个 132 模式的的子序列：[-1, 3, 2]、[-1, 3, 0] 和 [-1, 2, 0] 。

提示：
n == nums.length
1 <= n <= 104
-109 <= nums[i] <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/132-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

from sortedcontainers import SortedList


class Solution(object):
    def find132pattern(self, nums):
        """
        这个方法就是 O(N^2)的解法，是这个题的暴力解法。

        我选择的方法是维护 132模式 中间的那个数字 3，因为 3 在 132 的中间的数字、也是最大的数字。
        我们的思路是个贪心的方法：我们要维护的 1 是 3 左边的最小的数字； 2 是 3 右边的比 3 小并且比 1 大的数字。

        从左到右遍历一次，遍历的数字是nums[j] 也就是 132 模式中的 3。
        根据上面的贪心思想分析，我们想让 1 是 3 左边最小的元素，然后使用暴力在nums[j+1..N−1] 中找到 132 模式中的 2 就行。

        这个思路比较简单，也能 AC。
        """
        N = len(nums)
        numsi = nums[0]
        for j in range(1, N):
            for k in range(N - 1, j, -1):
                if numsi < nums[k] and nums[k] < nums[j]:
                    return True
            numsi = min(numsi, nums[j])
        return False

    def find132pattern(self, nums):
        """
        求任何位置的左边最小的元素 nums[i]，可以提前遍历一次而得到；
        使用「单调递减栈」，把 nums[j] 入栈时，需要把栈里面比它小的元素全都 pop 出来，
        由于越往栈底越大，所以 pop 出的最后一个元素，就是比 3 小的最大元素 nums[k]。
        判断如果 nums[i] < nums[k]，那就说明得到了一个 132 模式。
        因为单调栈是建立在 3 的右边的，因此，我们使用从右向左遍历。
        """
        N = len(nums)
        leftMin = [float("inf")] * N
        for i in range(1, N):
            leftMin[i] = min(leftMin[i - 1], nums[i - 1])
        stack = []
        for j in range(N - 1, -1, -1):
            numsk = float("-inf")
            while stack and stack[-1] < nums[j]:
                numsk = stack.pop()
            if leftMin[j] < numsk:
                return True
            stack.append(nums[j])
        return False


class Solution:
    """
    方法一：枚举 3
    思路与算法

    枚举 3 是容易想到并且也是最容易实现的。由于 3 是模式中的最大值，并且其出现在 1 和 2 的中间，因此我们只需要从左到右枚举 3 的下标 j，那么：

    由于 1 是模式中的最小值，因此我们在枚举 j 的同时，维护数组 a 中左侧元素 a[0..j-1]的最小值，即为 1 对应的元素 a[i]。
    需要注意的是，只有 a[i] < a[j] 时，a[i] 才能作为 1 对应的元素；

    由于 2 是模式中的次小值，因此我们可以使用一个有序集合（例如平衡树）维护数组 a 中右侧元素 a[j+1..n−1] 中的所有值。
    当我们确定了 a[i] 和 a[j] 之后，只需要在有序集合中查询严格比 a[i] 大的那个最小的元素，即为 a[k]。需
    要注意的是，只有 a[k] < a[j] 时，a[k]才能作为 33 对应的元素。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/132-pattern/solution/132mo-shi-by-leetcode-solution-ye89/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        # 左侧最小值
        left_min = nums[0]
        # 右侧所有元素
        right_all = SortedList(nums[2:])

        for j in range(1, n - 1):
            if left_min < nums[j]:
                index = right_all.bisect_right(left_min)
                if index < len(right_all) and right_all[index] < nums[j]:
                    return True
            left_min = min(left_min, nums[j])
            right_all.remove(nums[j + 1])

        return False


class Solution:
    """
    方法二：枚举 11
    思路与算法

    如果我们从左到右枚举 1 的下标 i，那么 j, k 的下标范围都是减少的，这样就不利于对它们进行维护。因此我们可以考虑从右到左枚举 i。
    那么我们应该如何维护 j, k呢？在 132模式中，如果 1<2并且 2<3，那么根据传递性，1<3 也是成立的，那么我们可以使用下面的方法进行维护：
    我们使用一种数据结构维护所有遍历过的元素，它们作为 2 的候选元素。每当我们遍历到一个新的元素时，就将其加入数据结构中；
    在遍历到一个新的元素的同时，我们可以考虑其是否可以作为 3。如果它作为 3，那么数据结构中所有严格小于它的元素都可以作为 2，
    我们将这些元素全部从数据结构中移除，并且使用一个变量维护所有被移除的元素的最大值。这些被移除的元素都是可以真正作为 2 的，
    并且元素的值越大，那么我们之后找到 1 的机会也就越大。

    那么这个「数据结构」是什么样的数据结构呢？我们尝试提取出它进行的操作：
    它需要支持添加一个元素；
    它需要支持移除所有严格小于给定阈值的所有元素；
    上面两步操作是「依次进行」的，即我们先用给定的阈值移除元素，再将该阈值加入数据结构中。
    这就是「单调栈」。在单调栈中，从栈底到栈顶的元素是严格单调递减的。当给定阈值 x 时，我们只需要不断地弹出栈顶的元素，
    直到栈为空或者 x 严格小于栈顶元素。此时我们再将 x 入栈，这样就维护了栈的单调性。

    因此，我们可以使用单调栈作为维护 2 的数据结构，并给出下面的算法：
    我们用单调栈维护所有可以作为 2 的候选元素。初始时，单调栈中只有唯一的元素 a[n−1]。
    我们还需要使用一个变量 max_k 记录所有可以真正作为 2 的元素的最大值；

    随后我们从 n-2 开始从右到左枚举元素 a[i]：

    首先我们判断 a[i] 是否可以作为 1。如果a[i]<max_k，那么它就可以作为 1，我们就找到了一组满足 132 模式的三元组；

    随后我们判断 a[i] 是否可以作为 3，以此找出哪些可以真正作为 2 的元素。我们将 a[i]不断地与单调栈栈顶的元素进行比较，
    如果 a[i] 较大，那么栈顶元素可以真正作为 2，将其弹出并更新 max_k；

    最后我们将 a[i] 作为 2 的候选元素放入单调栈中。这里可以进行一个优化，即如果 a[i]≤max_k，
    那么我们也没有必要将 a[i] 放入栈中，因为即使它在未来被弹出，也不会将 max_k 更新为更大的值。

    在枚举完所有的元素后，如果仍未找到满足 132 模式的三元组，那就说明其不存在。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/132-pattern/solution/132mo-shi-by-leetcode-solution-ye89/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        candidate_k = [nums[n - 1]]
        max_k = float("-inf")

        for i in range(n - 2, -1, -1):
            if nums[i] < max_k:
                return True
            while candidate_k and nums[i] > candidate_k[-1]:
                max_k = candidate_k[-1]
                candidate_k.pop()
            if nums[i] > max_k:
                candidate_k.append(nums[i])

        return False
