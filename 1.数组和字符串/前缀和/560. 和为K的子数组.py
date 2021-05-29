"""
给定一个整数数组和一个整数k，你需要找到该数组中和为k的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数k的范围是[-1e7, 1e7]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        import collections
        # num_times 存储某“前缀和”出现的次数，这里用collections.defaultdict来定义它
        # 如果某前缀不在此字典中，那么它对应的次数为0
        num_times = collections.defaultdict(int)
        num_times[0] = 1  # 先给定一个初始值，代表前缀和为0的出现了一次
        cur_sum = 0  # 记录到当前位置的前缀和
        res = 0
        for i in range(len(nums)):
            cur_sum += nums[i]  # 计算当前前缀和
            if cur_sum - k in num_times:  # 如果前缀和减去目标值k所得到的值在字典中出现，即当前位置前缀和减去之前某一位的前缀和等于目标值
                res += num_times[cur_sum - k]
            # 下面一句实际上对应两种情况，一种是某cur_sum之前出现过（直接在原来出现的次数上+1即可），
            # 另一种是某cur_sum没出现过（理论上应该设为1，但是因为此处用defaultdict存储，如果cur_sum这个key不存在将返回默认的int，也就是0）
            # 返回0加上1和直接将其置为1是一样的效果。所以这里统一用一句话包含上述两种情况
            num_times[cur_sum] += 1
        return res


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums_dict = {}
        nums_sum = count = 0
        for num in nums:
            nums_sum += num
            if nums_sum == k:
                count += 1
            if nums_sum - k in nums_dict:
                count += nums_dict[nums_sum - k]
            if nums_sum in nums_dict:
                nums_dict[nums_sum] += 1
            else:
                nums_dict[nums_sum] = 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.subarraySum(nums=[1, 1, 1], k=2))  # 2
    print(s.subarraySum(nums=[1, 1, 1], k=0))  # 0
    print(s.subarraySum(nums=[1, 1, 1], k=1))  # 3
    print(s.subarraySum(nums=[0, 0, 0], k=0))
    print(s.subarraySum([-1, -1, 1], 0))
