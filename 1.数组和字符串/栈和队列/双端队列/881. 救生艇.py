"""
第i个人的体重为people[i]，每艘船可以承载的最大重量为limit。
每艘船最多可同时载两人，但条件是这些人的重量之和最多为limit。
返回载到每一个人所需的最小船数。(保证每个人都能被船载)。

示例 1：
输入：people = [1,2], limit = 3
输出：1
解释：1 艘船载 (1, 2)
示例 2：
输入：people = [3,2,2,1], limit = 3
输出：3
解释：3 艘船分别载 (1, 2), (2) 和 (3)
示例 3：
输入：people = [3,5,3,4], limit = 5
输出：4
解释：4 艘船分别载 (3), (3), (4), (5)
提示：

1 <=people.length <= 50000
1 <= people[i] <=limit <= 30000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/boats-to-save-people
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
from collections import deque


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        dq = deque(sorted(people))
        ans = 0
        while dq:
            p1 = dq.pop()
            if dq and p1 + dq[0] <= limit:
                dq.popleft()
            ans += 1
        return ans


class Solution(object):
    """
    方法：贪心（双指针）
    思路
    如果最重的人可以与最轻的人共用一艘船，那么就这样安排。否则，最重的人无法与任何人配对，那么他们将自己独自乘一艘船。
    这么做的原因是，如果最轻的人可以与任何人配对，那么他们也可以与最重的人配对。
    算法
    令 people[i] 指向当前最轻的人，而 people[j] 指向最重的那位。
    然后，如上所述，如果最重的人可以与最轻的人共用一条船（即 people[j] + people[i] <= limit），那么就这样做；
    否则，最重的人自己独自坐在船上。

    作者：LeetCode
    链接：https://leetcode-cn.com/problems/boats-to-save-people/solution/jiu-sheng-ting-by-leetcode/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def numRescueBoats(self, people, limit):
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numRescueBoats(people=[1, 2], limit=3))
    print(s.numRescueBoats(people=[3, 2, 2, 1], limit=3))
    print(s.numRescueBoats(people=[3, 5, 3, 4], limit=5))
