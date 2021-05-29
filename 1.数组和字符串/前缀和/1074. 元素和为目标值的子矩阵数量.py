"""
给出矩阵matrix和目标值target，返回元素总和等于目标值的非空子矩阵的数量。

子矩阵x1, y1, x2, y2是满足 x1 <= x <= x2且y1 <= y <= y2的所有单元matrix[x][y]的集合。

如果(x1, y1, x2, y2) 和(x1', y1', x2', y2')两个子矩阵中部分坐标不同（如：x1 != x1'），那么这两个子矩阵也不同。



示例 1：



输入：matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
输出：4
解释：四个只含 0 的 1x1 子矩阵。
示例 2：

输入：matrix = [[1,-1],[-1,1]], target = 0
输出：5
解释：两个 1x2 子矩阵，加上两个 2x1 子矩阵，再加上一个 2x2 子矩阵。
示例 3：

输入：matrix = [[904]], target = 0
输出：0


提示：

1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-submatrices-that-sum-to-target
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import Counter
from typing import List


class Solution:
    """
    方法一：前缀和 + 哈希表
    我们枚举子矩阵的上下边界，并计算出该边界内每列的元素和，则原问题转换成了如下一维问题：

    给定一个整数数组和一个整数target，计算该数组中子数组和等于target 的子数组个数。

    力扣上已有该问题：560. 和为K的子数组，读者可以参考其官方题解，并掌握使用前缀和+哈希表的线性做法。

    对于每列的元素和 sum 的计算，我们在枚举子矩阵上边界 i 时，初始下边界 j 为 i，此时 sum 就是矩阵第 i 行的元素。
    每次向下延长下边界 j 时，我们可以将矩阵第 j 行的元素累加到 sum 中。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/number-of-submatrices-that-sum-to-target/solution/yuan-su-he-wei-mu-biao-zhi-de-zi-ju-zhen-8ym2/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def subarraySum(nums: List[int], k: int) -> int:
            mp = Counter([0])
            count = pre = 0
            for x in nums:
                pre += x
                if pre - k in mp:
                    count += mp[pre - k]
                mp[pre] += 1
            return count

        m, n = len(matrix), len(matrix[0])
        ans = 0
        # 枚举上边界
        for i in range(m):
            total = [0] * n
            # 枚举下边界
            for j in range(i, m):
                for c in range(n):
                    # 更新每列的元素和
                    total[c] += matrix[j][c]
                ans += subarraySum(total, target)

        return ans


from collections import Counter


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def subarraySum(nums: List[int], k: int) -> int:
            mp = Counter([0])  # 使用这个或者defaultdict的好处就是可以避免KeyError,也就是键不存在时访问报错
            count, pre = 0, 0
            for num in nums:
                pre += num
                if pre - k in mp:
                    count += mp[pre - k]
                mp[pre] += 1
            return count

        """
        思路：就是只要考虑上下边界就可，以3*3为例，起始位置如果是第一行，结束位置可以是第一行，第二行，第三行
            这样在第一行情况时，将列和统计一下，就是一个一维数组，使用560题的判断方法即可，子数组的动态移动将控制子矩阵的列数
            在前两行时，再将列和累加，判断前两行的子矩阵，
            前三行道理相同

            接下来更新起始行，就可以考虑到第二行，二三行，继而更新考虑到第三行
        """
        m, n = len(matrix), len(matrix[0])  # 统计矩阵的行和列
        ans = 0  # 记录符合条件的结果
        for i in range(m):  # 起始行 i
            total = [0] * n
            for j in range(i, m):  # 结束行 j
                for c in range(n):  # 统计列和
                    total[c] += matrix[j][c]
                ans += subarraySum(total, target)  # 统计完一次记得统计起始行和结束行范围内符合条件的子矩阵和
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numSubmatrixSumTarget([[0, 1, 0], [1, 1, 1], [0, 1, 0]]))
