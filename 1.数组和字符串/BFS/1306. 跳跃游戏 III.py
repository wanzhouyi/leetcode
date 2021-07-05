"""
这里有一个非负整数数组arr，你最开始位于该数组的起始下标start处。当你位于下标i处时，你可以跳到i + arr[i] 或者 i - arr[i]。
请你判断自己是否能够跳到对应元素值为 0 的 任一 下标处。
注意，不管是什么情况下，你都无法跳到数组之外。

示例 1：
输入：arr = [4,2,3,0,3,1,2], start = 5
输出：true
解释：
到达值为 0 的下标 3 有以下可能方案： 
下标 5 -> 下标 4 -> 下标 1 -> 下标 3 
下标 5 -> 下标 6 -> 下标 4 -> 下标 1 -> 下标 3 

示例 2：
输入：arr = [4,2,3,0,3,1,2], start = 0
输出：true 
解释：
到达值为 0 的下标 3 有以下可能方案： 
下标 0 -> 下标 4 -> 下标 1 -> 下标 3

示例 3：
输入：arr = [3,0,2,1,2], start = 2
输出：false
解释：无法到达值为 0 的下标 1 处。 

提示：

1 <= arr.length <= 5 * 10^4
0 <= arr[i] <arr.length
0 <= start < arr.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        stack = [start]
        visited = set()
        while stack:
            temp_stack = stack.copy()
            stack.clear()
            for index in temp_stack:
                visited.add(index)
                if arr[index] == 0:
                    return True
                add = index + arr[index]
                if 0 <= add < n and add not in visited:
                    stack.append(add)
                sub = index - arr[index]
                if 0 <= sub < n and sub not in visited:
                    stack.append(sub)
        return False


# 官解
class Solution:
    """
    方法一：广度优先搜索
    我们可以使用广度优先搜索的方法得到从 start 开始能够到达的所有位置，如果其中某个位置对应的元素值为 0，那么就返回 True。

    具体地，我们初始时将 start 加入队列。在每一次的搜索过程中，我们取出队首的节点 u，它可以到达的位置为 u + arr[u] 和 u - arr[u]。如果某个位置落在数组的下标范围 [0, len(arr)) 内，并且没有被搜索过，则将该位置加入队尾。只要我们搜索到一个对应元素值为 0 的位置，我们就返回 True。在搜索结束后，如果仍然没有找到符合要求的位置，我们就返回 False。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/jump-game-iii/solution/tiao-yue-you-xi-iii-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True

        n = len(arr)
        used = {start}
        q = collections.deque([start])

        while len(q) > 0:
            u = q.popleft()
            for v in [u + arr[u], u - arr[u]]:
                if 0 <= v < n and v not in used:
                    if arr[v] == 0:
                        return True
                    q.append(v)
                    used.add(v)

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=5))
    print(s.canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=0))
    print(s.canReach(arr=[3, 0, 2, 1, 2], start=2))
