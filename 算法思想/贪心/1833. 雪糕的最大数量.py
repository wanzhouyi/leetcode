"""
夏日炎炎，小男孩 Tony 想买一些雪糕消消暑。

商店中新到 n 支雪糕，用长度为 n 的数组 costs 表示雪糕的定价，其中 costs[i] 表示第 i 支雪糕的现金价格。Tony 一共有 coins 现金可以用于消费，他想要买尽可能多的雪糕。

给你价格数组 costs 和现金量 coins ，请你计算并返回 Tony 用 coins 现金能够买到的雪糕的 最大数量 。

注意：Tony 可以按任意顺序购买雪糕。



示例 1：

输入：costs = [1,3,2,4,1], coins = 7
输出：4
解释：Tony 可以买下标为 0、1、2、4 的雪糕，总价为 1 + 3 + 2 + 1 = 7
示例 2：

输入：costs = [10,6,8,7,7,8], coins = 5
输出：0
解释：Tony 没有足够的钱买任何一支雪糕。
示例 3：

输入：costs = [1,6,3,1,2,5], coins = 20
输出：6
解释：Tony 可以买下所有的雪糕，总价为 1 + 6 + 3 + 1 + 2 + 5 = 18 。


提示：

costs.length == n
1 <= n <= 105
1 <= costs[i] <= 105
1 <= coins <= 108

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-ice-cream-bars
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    """
    在给定硬币数量coins 的情况下，要买到最多的雪糕，应该买最便宜的雪糕，理由如下。

    假设购买最便宜的雪糕，在总价格不超过coins 的情况下最多可以购买 k 支雪糕。
    如果将 k 支最便宜的雪糕中的任意一支雪糕替换成另一支雪糕，则替换后的雪糕的价格大于或等于替换前的雪糕的价格，
    因此替换后的总价格大于或等于替换前的总价格，允许购买的雪糕数量不可能超过 k。因此可以买到的雪糕的最大数量为 k。

    由此可以得到贪心的解法：对数组 costs 排序，然后按照从小到大的顺序遍历数组元素，
    对于每个元素，如果该元素不超过剩余的硬币数，则将硬币数减去该元素值，表示购买了这支雪糕，
    当遇到一个元素超过剩余的硬币数时，结束遍历，此时购买的雪糕数量即为可以购买雪糕的最大数量。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/maximum-ice-cream-bars/solution/xue-gao-de-zui-da-shu-liang-by-leetcode-ia3m7/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cnt = 0
        while costs:
            curr = costs.pop(0)
            if curr <= coins:
                cnt += 1
                coins -= curr
            else:
                break
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.maxIceCream(costs=[1, 3, 2, 4, 1], coins=7))
    print(s.maxIceCream(costs=[10, 6, 8, 7, 7, 8], coins=5))
    print(s.maxIceCream(costs=[1, 6, 3, 1, 2, 5], coins=20))
