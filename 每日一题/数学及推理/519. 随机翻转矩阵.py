"""
给你一个 m x n 的二元矩阵 matrix ，且所有值被初始化为 0 。
请你设计一个算法，随机选取一个满足matrix[i][j] == 0 的下标(i, j) ，并将它的值变为 1 。
所有满足 matrix[i][j] == 0 的下标 (i, j) 被选取的概率应当均等。
尽量最少调用内置的随机函数，并且优化时间和空间复杂度。

实现 Solution 类：

Solution(int m, int n) 使用二元矩阵的大小 m 和 n 初始化该对象
int[] flip() 返回一个满足matrix[i][j] == 0 的随机下标 [i, j] ，并将其对应格子中的值变为 1
void reset() 将矩阵中所有的值重置为 0

示例：
输入
["Solution", "flip", "flip", "flip", "reset", "flip"]
[[3, 1], [], [], [], [], []]
输出
[null, [1, 0], [2, 0], [0, 0], null, [2, 0]]

解释
Solution solution = new Solution(3, 1);
solution.flip();  // 返回 [1, 0]，此时返回 [0,0]、[1,0] 和 [2,0] 的概率应当相同
solution.flip();  // 返回 [2, 0]，因为 [1,0] 已经返回过了，此时返回 [2,0] 和 [0,0] 的概率应当相同
solution.flip();  // 返回 [0, 0]，根据前面已经返回过的下标，此时只能返回 [0,0]
solution.reset(); // 所有值都重置为 0 ，并可以再次选择下标返回
solution.flip();  // 返回 [2, 0]，此时返回 [0,0]、[1,0] 和 [2,0] 的概率应当相同

提示：
1 <= m, n <= 104
每次调用flip 时，矩阵中至少存在一个值为 0 的格子。
最多调用 1000 次 flip 和 reset 方法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/random-flip-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import math
from random import random
from typing import List

"""
我们可以考虑另一种方法来维护这个一维数组 map。假设我们把这 m×n 个位置放到 k 个桶中，第一个桶对应 map[0⋯a1 ]，
第二个桶对应 map[a1+1⋯a2 ]，以此类推。我们用 cnt[i] 表示第 i 个桶中还剩余的 0 的个数，
并给每个桶分配一个集合 HashSet 存放桶中哪些位置对应的是 1（即被翻转过的位置）。
假设当前矩阵中还有 total 个 0，我们从 [1,total] 中随机出一个整数 x，并遍历所有的桶，根据所有的 cnt[i] 可以找出第 x 个 0 属于哪个桶。
假设其属于第 i 个桶，那么 x 应该满足 sum[i−1]<x<=sum[i]，其中sum[i] 表示前 i 个桶的 cnt[i] 之和，即前 i 个桶中 0 的个数。
随后我们令 y=x−sum[i−1]，即我们需要找到第 i 个桶中的第 y 个 0。我们可以依次遍历[d×i+1⋯d×(i+1)] 中的数，根据第 i 个桶对应的集合，找出第 y 个 0 的位置。
最后我们将这个00 进行翻转。

由于 map 被分成了 k 个桶，因此每个桶的平均长度为m×n/k。在上述的方法中，遍历所有的桶的时间复杂度为 O(k)，
而遍历第 i 个桶的时间复杂度为 O(m×n/k)，因此总时间复杂度为 O(k + m×n/k)。根据均值不等式，可以得知在 k= m×n**0.5 ，总的时间复杂度最小。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/random-flip-matrix/solution/sui-ji-fan-zhuan-ju-zhen-by-leetcode-sol-pfmr/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:
    def __init__(self, m: int, n: int):
        self.m, self.n = m, n
        self.total = m * n
        self.bucketSize = math.floor(math.sqrt(m * n))
        self.buckets = [set() for _ in range(0, self.total, self.bucketSize)]

    def flip(self) -> List[int]:
        x = random.randint(0, self.total - 1)
        self.total -= 1
        sumZero = 0
        curr = 0

        for i in range(len(self.buckets)):
            if sumZero + self.bucketSize - len(self.buckets[i]) > x:
                for j in range(self.bucketSize):
                    if (curr + j) not in self.buckets[i]:
                        if sumZero == x:
                            self.buckets[i].add(curr + j)
                            return [(curr + j) // self.n, (curr + j) % self.n]
                        sumZero += 1
            curr += self.bucketSize
            sumZero += self.bucketSize - len(self.buckets[i])
        return []

    def reset(self) -> None:
        self.total = self.m * self.n
        for i in range(len(self.buckets)):
            self.buckets[i].clear()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
if __name__ == '__main__':
    s = Solution(10000, 10000)
    for _ in range(10):
        print(s.flip())
