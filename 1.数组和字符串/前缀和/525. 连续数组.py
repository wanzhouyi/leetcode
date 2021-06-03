"""
给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
示例 1:
输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
示例 2:

输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。

提示：

1 <= nums.length <= 105
nums[i] 不是 0 就是 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contiguous-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    """
    使用字典记录每个1的数量和0的数量的差值最早出现的位置,使用前缀和变量统计从开始到现在的1的数量和0的数量的差值。

    为什么这么做呢？先不考虑最长的问题。
    想一想如果两个位置的1的数量和0的数量的差值相等，意味着什么？
    假设这个差值是k,左边位置x有m个0,可知x有m+k个1（保证数量差值为k）；同时假设右边位置y有n个0，可知y有n+k个1。
    那么可以知道(x,y]（左开右闭）里，0的数量为n-m,1的数量为n+k-m-k=n-m，
    故满足1和0数量的差值相等的两个位置 的充分必要条件是: 他们之间0和1的数量相同。

    那么现在要想找最长，我们肯定希望左边的位置尽可能靠左，所以我们在更新的时候，出现在字典中的相同值不再更新！只是统计一下长度大小。

    作者：qubenhao
    链接：https://leetcode-cn.com/problems/contiguous-array/solution/python-qian-zhui-he-bian-liang-zi-dian-b-9oct/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def findMaxLength(self, nums: List[int]) -> int:
        # 前缀和字典: key为1的数量和0的数量的差值,value为对应坐标
        hashmap = {0: -1}
        # 当前1的数量和0的数量的差值
        counter = ans = 0
        for i, num in enumerate(nums):
            # 每多一个1，差值+1
            if num:
                counter += 1
            # 每多一个0，差值-1
            else:
                counter -= 1
            # 如果存在1和0的数量差值相等的地方，那么说明后者到前者之前1和0的数量相等！
            if counter in hashmap:
                ans = max(ans, i - hashmap[counter])
            else:
                hashmap[counter] = i
        return ans
