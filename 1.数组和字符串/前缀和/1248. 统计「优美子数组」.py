"""
给你一个整数数组nums 和一个整数 k。

如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。

请返回这个数组中「优美子数组」的数目。



示例 1：

输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
示例 2：

输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
示例 3：

输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16


提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-number-of-nice-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        计算前缀和数组 arr：遍历原数组，每遍历一个元素，计算当前的前缀和（即到当前元素为止，数组中有多少个奇数）；
        对上述前缀和数组，双重循环统计 arr[j] - arr[i] == k 的个数，这样做是 O(N^2)的（这里会超时哦）。
        优化：因此，我们可以像「1. 两数之和」那样使用 HashMap 优化到 O(N)，
        键是「前缀和」，值是「前缀和的个数」（下面代码中具体使用的是 int[] prefixCnt 数组，
        下标是「前缀和」，值是「前缀和的个数」），因此我们可以遍历原数组，每遍历到一个元素，计算当前的前缀和 sum，
        就在 res 中累加上前缀和为 sum - k 的个数。
        """
        # 数组 prefixCnt 的下标是前缀和（即当前奇数的个数），值是前缀和的个数。
        prefix_cnt = [0] * (len(nums) + 1)
        prefix_cnt[0] = 1
        # 遍历原数组，计算当前的前缀和，统计到 prefixCnt 数组中，
        # 并且在 res 中累加上与当前前缀和差值为 k 的前缀和的个数。
        res, sum = 0, 0
        for num in nums:
            sum += num & 1
            prefix_cnt[sum] += 1
            if sum >= k:
                res += prefix_cnt[sum - k]
        return res


class Solution:
    """
    这个题应该是比较标准的数组前缀和的题，560. 和为K的子数组很像，但应该还要简单一点。
    题解参考560. 和为K的子数组 前缀和
    需要注意的是，这道题的前缀和是单调不减的，建哈希表更简单，初始化{0：1}表示什么数都不选已经有一种无奇数情况了。

    作者：zxnian_ustc
    链接：https://leetcode-cn.com/problems/count-number-of-nice-subarrays/solution/1248-tong-ji-you-mei-zi-shu-zu-qian-zhui-9o2p/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums_new = list(map(lambda x: 0 if x % 2 == 0 else 1, nums))
        pre_sum = 0
        dic = {0: 1}
        ans = 0
        for num in nums_new:
            temp_sum = pre_sum + num
            if dic.get(temp_sum):
                dic[temp_sum] += 1
            else:
                dic[temp_sum] = 1
            pre_sum = temp_sum

            if dic.get(temp_sum - k):
                ans += dic[temp_sum - k]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfSubarrays(nums=[1, 1, 2, 1, 1], k=3))
    print(s.numberOfSubarrays(nums=[2, 4, 6], k=1))
