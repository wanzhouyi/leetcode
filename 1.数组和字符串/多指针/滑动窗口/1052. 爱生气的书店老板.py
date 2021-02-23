"""
今天，书店老板有一家店打算试营业customers.length分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。
在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。
书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续X 分钟不生气，但却只能使用一次。
请你返回这一天营业下来，最多有多少客户能够感到满意的数量。

示例：

输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
输出：16
解释：
书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.

提示：

1 <= X <=customers.length ==grumpy.length <= 20000
0 <=customers[i] <= 1000
0 <=grumpy[i] <= 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/grumpy-bookstore-owner
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 滑动窗口
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        base_sum = sum([customers[idx] for idx, grum in enumerate(grumpy) if grum == 0])
        base_add = sum([customers[idx] for idx in range(X) if grumpy[idx] == 1])
        to_add = base_add

        left = 0
        for right in range(X, len(customers)):
            if grumpy[right] == 1:
                base_add += customers[right]
            if grumpy[left] == 1:
                base_add -= customers[left]
            left += 1
            to_add = max(base_add, to_add)

        return base_sum + to_add
