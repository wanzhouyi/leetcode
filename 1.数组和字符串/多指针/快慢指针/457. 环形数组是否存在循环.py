"""
存在一个不含 0 的 环形 数组nums ，每个 nums[i] 都表示位于下标 i 的角色应该向前或向后移动的下标个数：

如果 nums[i] 是正数，向前 移动 nums[i] 步
如果nums[i] 是负数，向后 移动 nums[i] 步
因为数组是 环形 的，所以可以假设从最后一个元素向前移动一步会到达第一个元素，而第一个元素向后移动一步会到达最后一个元素。

数组中的 循环 由长度为 k 的下标序列 seq ：

遵循上述移动规则将导致重复下标序列 seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
所有 nums[seq[j]] 应当不是 全正 就是 全负
k > 1
如果 nums 中存在循环，返回 true ；否则，返回 false 。



示例 1：

输入：nums = [2,-1,1,2,2]
输出：true
解释：存在循环，按下标 0 -> 2 -> 3 -> 0 。循环长度为 3 。
示例 2：

输入：nums = [-1,2]
输出：false
解释：按下标 1 -> 1 -> 1 ... 的运动无法构成循环，因为循环的长度为 1 。根据定义，循环的长度必须大于 1 。
示例 3:

输入：nums = [-2,1,-1,-2,-2]
输出：false
解释：按下标 1 -> 2 -> 1 -> ... 的运动无法构成循环，因为 nums[1] 是正数，而 nums[2] 是负数。
所有 nums[seq[j]] 应当不是全正就是全负。


提示：

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
nums[i] != 0


进阶：你能设计一个时间复杂度为 O(n) 且额外空间复杂度为 O(1) 的算法吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/circular-array-loop
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    """
    方法一：快慢指针
    思路及算法
    我们可以将环形数组理解为图中的 n 个点，nums[i] 表示i 号点向 (i+nums[i]) mod n 号点连有一条单向边。
    注意到这张图中的每个点有且仅有一条出边，这样我们从某一个点出发，沿着单向边不断移动，最终必然会进入一个环中。
    而依据题目要求，我们要检查图中是否存在一个所有单向边方向一致的环。
    我们可以使用在无向图中找环的一个经典算法：快慢指针来解决本题，参考题解「141. 环形链表」。

    具体地，我们检查每一个节点，令快慢指针从当前点出发，快指针每次移动两步，
    慢指针每次移动一步，期间每移动一次，我们都需要检查当前单向边的方向是否与初始方向是否一致，
    如果不一致，我们即可停止遍历，因为当前路径必然不满足条件。
    为了降低时间复杂度，我们可以标记每一个点是否访问过，过程中如果我们的下一个节点为已经访问过的节点，则可以停止遍历。
    在实际代码中，我们无需新建一个数组记录每个点的访问情况，而只需要将原数组的对应元素置零即可（题目保证原数组中元素不为零）。
    遍历过程中，如果快慢指针相遇，或者移动方向改变，那么我们就停止遍历，并将快慢指针经过的点均置零即可。

    特别地，当 nums[i] 为 n 的整倍数时，i 的后继节点即为 i 本身，
    此时循环长度 k=1，不符合题目要求，因此我们需要跳过这种情况。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/circular-array-loop/solution/huan-xing-shu-zu-shi-fou-cun-zai-xun-hua-0ay2/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next(cur: int) -> int:
            return (cur + nums[cur]) % n  # 保证返回值在 [0,n) 中

        for i, num in enumerate(nums):
            if num == 0:
                continue
            slow, fast = i, next(i)
            # 判断非零且方向相同
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next(fast)] > 0:
                if slow == fast:
                    if slow == next(slow):
                        break
                    return True
                slow = next(slow)
                fast = next(next(fast))
            add = i
            while nums[add] * nums[next(add)] > 0:
                tmp = add
                add = next(add)
                nums[tmp] = 0
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.circularArrayLoop(nums=[2, -1, 1, 2, 2]))
    # print(s.circularArrayLoop(nums=[-1, 2, -1, 1, 2, 2]))
    # print(s.circularArrayLoop(nums = [-1,2]))
