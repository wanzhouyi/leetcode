"""
在经典汉诺塔问题中，有 3 根柱子及 N 个不同大小的穿孔圆盘，盘子可以滑入任意一根柱子。一开始，所有盘子自上而下按升序依次套在第一根柱子上(即每一个盘子只能放在更大的盘子上面)。移动圆盘时受到以下限制:
(1) 每次只能移动一个盘子;
(2) 盘子只能从柱子顶端滑出移到下一根柱子;
(3) 盘子只能叠在比它大的盘子上。
请编写程序，用栈将所有盘子从第一根柱子移到最后一根柱子。
你需要原地修改栈。
示例1:
 输入：A = [2, 1, 0], B = [], C = []
 输出：C = [2, 1, 0]
示例2:
 输入：A = [1, 0], B = [], C = []
 输出：C = [1, 0]
提示:
A中盘子的数目不大于14个。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hanota-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        print('当前是', A, B, C)

        if len(A) == 1:
            C.append(A[0])
            A.clear()
            return

        self.hanota(A[1:], C, B)
        C.append(A[0])
        A.clear()
        self.hanota(B, A, C)

        print('结果是', A, B, C)


class Solution:
    """
    解题思路：递归与分治
    这是一道递归方法的经典题目，乍一想还挺难理清头绪的，我们不妨先从简单的入手。
    假设 n = 1,只有一个盘子，很简单，直接把它从 A 中拿出来，移到 C 上；
    如果 n = 2 呢？这时候我们就要借助 B 了，因为小盘子必须时刻都在大盘子上面，共需要 4 步。
    如果 n > 2 呢？思路和上面是一样的，我们把 n 个盘子也看成两个部分，一部分有 1 个盘子，另一部分有 n - 1 个盘子。=
    观察上图，你可能会问：“那 n - 1 个盘子是怎么从 A 移到 C 的呢？”
    注意，当你在思考这个问题的时候，就将最初的 n 个盘子从 A 移到 C 的问题，转化成了将 n - 1 个盘子从 A 移到 C 的问题，
    依次类推，直至转化成 1 个盘子的问题时，问题也就解决了。这就是分治的思想。

    而实现分治思想的常用方法就是递归。不难发现，如果原问题可以分解成若干个与原问题结构相同但规模较小的子问题时，往往可以用递归的方法解决。具体解决办法如下：

    n = 1 时，直接把盘子从 A 移到 C；
    n > 1 时，
        先把上面 n - 1 个盘子从 A 移到 B（子问题，递归）；
        再将最大的盘子从 A 移到 C；
        再将 B 上 n - 1 个盘子从 B 移到 C（子问题，递归）。

    作者：z1m
    链接：https://leetcode-cn.com/problems/hanota-lcci/solution/tu-jie-yi-nuo-ta-de-gu-shi-ju-shuo-dang-64ge-pan-z/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        n = len(A)
        self.move(n, A, B, C)

    # 定义move 函数移动汉诺塔
    def move(self, n, A, B, C):
        if n == 1:
            C.append(A[-1])
            A.pop()
            return
        else:
            self.move(n - 1, A, C, B)  # 将A上面n-1个通过C移到B
            C.append(A[-1])  # 将A最后一个移到C
            A.pop()  # 这时，A空了
            self.move(n - 1, B, A, C)  # 将B上面n-1个通过空的A移到C


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        n = len(A)
        if n == 1:
            C.append(A[0])
            A.pop()
            return
        B.extend(A[1:])
        C.append(A[0])
        A.clear()
        self.hanota(B, A, C)


if __name__ == '__main__':
    s = Solution()
    print(s.hanota([], [], []))
    print(s.hanota([1], [], []))
    print(s.hanota([2, 1], [], []))
    print(s.hanota([3, 2, 1], [], []))
    print(s.hanota([4, 3, 2, 1], [], []))
