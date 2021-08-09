"""
给你一个用字符数组tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。
然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
你需要计算完成所有任务所需要的 最短时间 。
示例 1：
输入：tasks = ["A","A","A","B","B","B"], n = 2
输出：8
解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B
     在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。 
示例 2：
输入：tasks = ["A","A","A","B","B","B"], n = 0
输出：6
解释：在这种情况下，任何大小为 6 的排列都可以满足要求，因为 n = 0
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
诸如此类
示例 3：

输入：tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
输出：16
解释：一种可能的解决方案是：
     A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> (待命) -> (待命) -> A -> (待命) -> (待命) -> A


提示：

1 <= task.length <= 10^4
tasks[i] 是大写英文字母
n 的取值范围为 [0, 100]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/task-scheduler
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ct = Counter(tasks)
        # print(ct)
        # print(ct.most_common(n))
        length = len(tasks)
        dic_ord = dict()
        ans = []
        while length > 0:
            mostn = [x[0] for x in ct.most_common(n + 1)] if n > 0 else list(ct.keys())
            for key in mostn:
                if key in dic_ord:
                    # 判断冷却期
                    # 如果差几个就加几个空的
                    chazhi = len(ans) - dic_ord[key] - 1
                    if chazhi < n:
                        ans.extend([''] * (n - chazhi))
                dic_ord[key] = len(ans)
                ans.append(key)
                ct[key] -= 1
                length -= 1
                if ct[key] == 0:
                    ct.pop(key)
        print(ans)
        return len(ans)


class Solution:
    """
    方法一：模拟
    思路与算法
    一种容易想到的方法是，我们按照时间顺序，依次给每一个时间单位分配任务。
    那么如果当前有多种任务不在冷却中，那么我们应该如何挑选执行的任务呢？
    直觉上，我们应当选择剩余执行次数最多的那个任务，将每种任务的剩余执行次数尽可能平均，使得 CPU 处于待命状态的时间尽可能少。
    当然这也是可以证明的，详细证明见下一个小标题。
    因此我们可以用二元组 (nextValid_i, rest_i)表示第 i 个任务，其中 nextValid_i表示其因冷却限制，
    最早可以执行的时间；rest_i表示其剩余执行次数。初始时，所有的 nextValid_i均为 1，
    而 rest_ir即为任务 i 在数组tasks 中出现的次数。

    我们用time 记录当前的时间。根据我们的策略，我们需要选择不在冷却中并且剩余执行次数最多的那个任务，
    也就是说，我们需要找到满足 nextValid_i≤time 的并且 rest_i最大的索引 i。
    因此我们只需要遍历所有的二元组，即可找到 i。
    在这之后，我们将 (nextValid_i, rest_i)更新为 (\textit{time}+n+1, \textit{rest}_i-1)(time+n+1,rest
    i
    ​
     −1)，记录任务 ii 下一次冷却结束的时间以及剩余执行次数。如果更新后的 \textit{rest}_i=0rest
    i
    ​
     =0，那么任务 ii 全部做完，我们在遍历二元组时也就可以忽略它了。

    而对于 \textit{time}time 的更新，我们可以选择将其不断增加 11，模拟每一个时间片。但这会导致我们在 CPU 处于待命状态时，对二元组进行不必要的遍历。为了减少时间复杂度，我们可以在每一次遍历之前，将 \textit{time}time 更新为所有 \textit{nextValid}_inextValid
    i
    ​
      中的最小值，直接「跳过」待命状态，保证每一次对二元组的遍历都是有效的。需要注意的是，只有当这个最小值大于 \textit{time}time 时，才需要这样快速更新。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/task-scheduler/solution/ren-wu-diao-du-qi-by-leetcode-solution-ur9w/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)

        # 任务总数
        m = len(freq)
        nextValid = [1] * m
        rest = list(freq.values())

        time = 0
        for i in range(len(tasks)):
            time += 1
            minNextValid = min(nextValid[j] for j in range(m) if rest[j] > 0)
            time = max(time, minNextValid)

            best = -1
            for j in range(m):
                if rest[j] and nextValid[j] <= time:
                    if best == -1 or rest[j] > rest[best]:
                        best = j

            nextValid[best] = time + n + 1
            rest[best] -= 1

        return time


if __name__ == '__main__':
    s = Solution()
    # print(s.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))
    print(s.leastInterval(tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2))
