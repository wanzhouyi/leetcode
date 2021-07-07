"""
大餐 是指 恰好包含两道不同餐品 的一餐，其美味程度之和等于 2 的幂。
你可以搭配 任意 两道餐品做一顿大餐。
给你一个整数数组 deliciousness ，其中 deliciousness[i] 是第 i 道餐品的美味程度，返回你可以用数组中的餐品做出的不同 大餐 的数量。
结果需要对 10^9 + 7 取余。

注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。

示例 1：
输入：deliciousness = [1,3,5,7,9]
输出：4
解释：大餐的美味程度组合为 (1,3) 、(1,7) 、(3,5) 和 (7,9) 。
它们各自的美味程度之和分别为 4 、8 、8 和 16 ，都是 2 的幂。

示例 2：
输入：deliciousness = [1,1,1,3,3,3,7]
输出：15
解释：大餐的美味程度组合为 3 种 (1,1) ，9 种 (1,3) ，和 3 种 (1,7) 。

提示：

1 <= deliciousness.length <= 105
0 <= deliciousness[i] <= 220

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-good-meals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from typing import List


class Solution:
    """
    第一版代码，纯粹的暴力解法，复杂度为n^2，超时。通过60/70
    """

    def countPairs(self, deliciousness: List[int]) -> int:
        n = len(deliciousness)
        cnt = 0
        pow2 = set()
        last = 1
        for i in range(22):
            pow2.add(last)
            last *= 2

        for i in range(n):
            for j in range(i + 1, n):
                if deliciousness[i] + deliciousness[j] in pow2:
                    cnt += 1
        return cnt


class Solution:
    """
    第二版代码，优化为一层循环，复杂度降低为n，但是循环内操作耗时，结果超时。
    求组合的代码超时比较多。通过66/70个用例
    """

    def countPairs(self, deliciousness: List[int]) -> int:
        cnt = 0
        pow2 = set()
        last = 1
        for i in range(22):
            pow2.add(last)
            last *= 2
        ct = Counter(deliciousness)
        # print(ct)
        deli_set = set(deliciousness)
        visited = set()
        for val in deli_set:
            for x in pow2:
                if x - val in deli_set:
                    if x - val == val and ct[val] > 1:
                        cnt += len(list(combinations([val] * ct[val], 2)))
                    elif x - val != val and x - val not in visited:
                        cnt += (ct[val] * ct[x - val])
                        visited.add(val)
        return cnt


class Solution:
    """
    第三版代码，变成解答错误了，通过69/70的用例。可见优化是有效果的。但是由于审题不严，需要再求余
    """

    def countPairs(self, deliciousness: List[int]) -> int:
        cnt = 0
        pow2 = set()
        last = 1

        @lru_cache(None)
        def get_combin(num):
            if num == 2:
                return 1
            return num - 1 + get_combin(num - 1)

        for i in range(22):
            pow2.add(last)
            last *= 2
        ct = Counter(deliciousness)
        print(ct)
        deli_set = set(deliciousness)
        visited = set()
        for val in deli_set:
            for x in pow2:
                if x - val in deli_set:
                    if x - val == val and ct[val] > 1:
                        cnt += get_combin(ct[val])
                    elif x - val != val and x - val not in visited:
                        cnt += (ct[val] * ct[x - val])
                        visited.add(val)
        return cnt


class Solution:
    """
    第四版代码，通过，超过98%
    """

    def countPairs(self, deliciousness: List[int]) -> int:
        cnt = 0
        pow2 = set()
        last = 1

        @lru_cache(None)
        def get_combin(num):
            if num == 2:
                return 1
            return num - 1 + get_combin(num - 1)

        for i in range(22):
            pow2.add(last)
            last *= 2
        ct = Counter(deliciousness)
        # print(ct)
        deli_set = set(deliciousness)
        visited = set()
        for val in deli_set:
            for x in pow2:
                if x - val in deli_set:
                    if x - val == val and ct[val] > 1:
                        cnt += get_combin(ct[val])
                    elif x - val != val and x - val not in visited:
                        cnt += (ct[val] * ct[x - val])
                        visited.add(val)
        return cnt % (10 ** 9 + 7)


# 好解
from collections import defaultdict


class Solution:
    """
    本题的基本思路可以拆解为：

    0 <= deliciousness[i] <= 2^20
    根据此条件，可以知道所谓2的幂是有限的，即：pows=[2^0, 2^1, 2^2, ..., 2**21]
    所以题目隐含的意思是，从数组中任选两个数，两数之和在上面的这个集合pows中
    对于相同的数字，根据排列组合公式，餐品的组合数是 n*(n-2)/2
    对于不同的数字，餐品的组合数是他们在输入数组中出现次数之乘机
    所以具体要做的事情是：

    统计数组，获取每一个数字出现的次数，得到一个次数字典ds_count
    对于ds_count中的每一个数字d，遍历2的幂集合pows，对于pows中每一个值p，若p-d存在于ds_count中，则(d, p-d)符合题目要求，根据思路2思路3可以得到它们组成大餐的数量
    遍历ds_count肯定会出现重复的记录，例如(1,3)和(3,1)，设置一个集合visited，来记录访问过的记录，避免重复

    作者：simonsun
    链接：https://leetcode-cn.com/problems/count-good-meals/solution/pythonyi-dian-yi-dian-you-hua-ji-bai-100-a0o2/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def countPairs(self, deliciousness: List[int]) -> int:
        ds_count = defaultdict(int)

        for d in deliciousness:
            ds_count[d] += 1

        pows = []
        for i in range(22):
            pows.append(2 ** i)

        result = 0
        visited = set()
        for d, count in ds_count.items():
            for p in pows:
                if p > d and p - d in ds_count:
                    if p - d == d:
                        result += int(count * (count - 1) / 2)
                    else:
                        key = f'{max(d, p - d)},{min(d, p - d)}'
                        if key not in visited:
                            visited.add(key)
                            result += ds_count[d] * ds_count[p - d]

        return result % 1000000007
