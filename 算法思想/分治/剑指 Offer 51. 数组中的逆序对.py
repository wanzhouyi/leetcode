"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数。

示例 1:
输入: [7,5,6,4]
输出: 5

限制：
0 <= 数组长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import bisect
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """
        这个思路就是反回来，换句话说，就是求右边比左边小的，于是先将右边的存到一个有序数组里，通过二分查找来降低复杂度
        """
        n = len(nums)
        arr = []
        ans = 0
        for i in range(n - 1, -1, -1):
            ans += bisect.bisect_left(arr, nums[i])
            bisect.insort(arr, nums[i])
        return ans


# 以下才是分治
class Solution:
    """
    方法一：归并排序
预备知识

「归并排序」是分治思想的典型应用，它包含这样三个步骤：

分解： 待排序的区间为 [l, r]，令 m=(l+r)/2，我们把 [l, r]分成 [l, m]和 [m + 1, r]
解决： 使用归并排序递归地排序两个子序列
合并： 把两个已经排好序的子序列 [l, m] 和 [m + 1, r] 合并起来
在待排序序列长度为 1 的时候，递归开始「回升」，因为我们默认长度为 1 的序列是排好序的。

思路

那么求逆序对和归并排序又有什么关系呢？关键就在于「归并」当中「并」的过程。
我们通过一个实例来看看。假设我们有两个已排序的序列等待合并，分别是 L={8,12,16,22,100} 和 R={9,26,55,64,91}。
一开始我们用指针 lPtr = 0 指向 L 的首部，rPtr = 0 指向 R 的头部。记已经合并好的部分为 M。


L = [8, 12, 16, 22, 100]   R = [9, 26, 55, 64, 91]  M = []
     |                          |
   lPtr                       rPtr
我们发现 lPtr 指向的元素小于 rPtr 指向的元素，于是把 lPtr 指向的元素放入答案，并把 lPtr 后移一位。


L = [8, 12, 16, 22, 100]   R = [9, 26, 55, 64, 91]  M = [8]
        |                       |
      lPtr                     rPtr
这个时候我们把左边的 8 加入了答案，我们发现右边没有数比 8 小，所以 8 对逆序对总数的「贡献」为 0。

接着我们继续合并，把 9 加入了答案，此时 lPtr 指向 12，rPtr 指向 26。


L = [8, 12, 16, 22, 100]   R = [9, 26, 55, 64, 91]  M = [8, 9]
        |                          |
       lPtr                       rPtr
此时 lPtr 比 rPtr 小，把 lPtr 对应的数加入答案，
并考虑它对逆序对总数的贡献为 rPtr 相对 R 首位置的偏移 1（即右边只有一个数比 12 小，所以只有它和 12 构成逆序对），以此类推。

我们发现用这种「算贡献」的思想在合并的过程中计算逆序对的数量的时候，
只在 lPtr 右移的时候计算，是基于这样的事实：
当前 lPtr 指向的数字比 rPtr 小，但是比 R 中 [0 ... rPtr - 1] 的其他数字大，[0 ... rPtr - 1] 的其他数字本应当排在 lPtr 对应数字的左边，但是它排在了右边，所以这里就贡献了 rPtr 个逆序对。

利用这个思路，我们可以写出如下代码。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/shu-zu-zhong-de-ni-xu-dui-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def mergeSort(self, nums, tmp, l, r):
        if l >= r:
            return 0

        mid = (l + r) // 2
        inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inv_count += (j - (mid + 1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            inv_count += (j - (mid + 1))
            pos += 1
        for k in range(j, r + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l:r + 1] = tmp[l:r + 1]
        return inv_count

    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = [0] * n
        return self.mergeSort(nums, tmp, 0, n - 1)


class Solution:
    """
    解题思路：
直观来看，使用暴力统计法即可，即遍历数组的所有数字对并统计逆序对数量。此方法时间复杂度为 O(N^2)，
观察题目给定的数组长度范围 0≤N≤50000 ，可知此复杂度是不能接受的。

「归并排序」与「逆序对」是息息相关的。归并排序体现了 “分而治之” 的算法思想，具体为：

分： 不断将数组从中点位置划分开（即二分法），将整个数组的排序问题转化为子数组的排序问题；
治： 划分到子数组长度为 1 时，开始向上合并，不断将 较短排序数组 合并为 较长排序数组，直至合并至原数组时完成排序；
如下图所示，为数组 [7, 3, 2, 6, 0, 1, 5, 4]的归并排序过程。



合并阶段 本质上是 合并两个排序数组 的过程，而每当遇到 左子数组当前元素 > 右子数组当前元素 时，
意味着 「左子数组当前元素 至 末尾元素」 与 「右子数组当前元素」 构成了若干 「逆序对」 。

如下图所示，为左子数组 [2, 3, 6, 7] 与 右子数组 [0, 1, 4, 5]的合并与逆序对统计过程。

因此，考虑在归并排序的合并阶段统计「逆序对」数量，完成归并排序时，也随之完成所有逆序对的统计。

算法流程：
merge_sort() 归并排序与逆序对统计：

终止条件： 当 l≥r 时，代表子数组长度为 1 ，此时终止划分；
递归划分： 计算数组中点 m ，递归划分左子数组 merge_sort(l, m) 和右子数组 merge_sort(m + 1, r) ；
合并与逆序对统计：
暂存数组 nums 闭区间 [i, r] 内的元素至辅助数组 tmp ；
循环合并： 设置双指针 i , j 分别指向左 / 右子数组的首元素；
当 i = m + 1 时： 代表左子数组已合并完，因此添加右子数组当前元素 tmp[j] ，并执行 j = j + 1 ；
否则，当 j = r + 1 时： 代表右子数组已合并完，因此添加左子数组当前元素 tmp[i] ，并执行 i = i + 1 ；
否则，当 tmp[i]≤tmp[j] 时： 添加左子数组当前元素 tmp[i] ，并执行 i = i + 1；
否则（即 tmp[i] > tmp[j]）时： 添加右子数组当前元素 tmp[j] ，并执行 j = j + 1 ；此时构成 m−i+1 个「逆序对」，统计添加至 resres ；
返回值： 返回直至目前的逆序对总数 resres ；
reversePairs() 主函数：

初始化： 辅助数组 tmptmp ，用于合并阶段暂存元素；
返回值： 执行归并排序 merge_sort() ，并返回逆序对总数即可；
如下图所示，为数组 [7, 3, 2, 6, 0, 1, 5, 4][7,3,2,6,0,1,5,4] 的归并排序与逆序对统计过程。



复杂度分析：
时间复杂度 O(N \log N)O(NlogN) ： 其中 NN 为数组长度；归并排序使用 O(N \log N)O(NlogN) 时间；
空间复杂度 O(N)O(N) ： 辅助数组 tmptmp 占用 O(N)O(N) 大小的额外空间；
代码：
为简化代码，「当 j = r + 1j=r+1 时」 与 「当 tmp[i] \leq tmp[j]tmp[i]≤tmp[j] 时」 两判断项可合并。

作者：jyd
链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/jian-zhi-offer-51-shu-zu-zhong-de-ni-xu-pvn2h/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(l, r):
            # 终止条件
            if l >= r: return 0
            # 递归划分
            m = (l + r) // 2
            res = merge_sort(l, m) + merge_sort(m + 1, r)
            # 合并阶段
            i, j = l, m + 1
            tmp[l:r + 1] = nums[l:r + 1]
            for k in range(l, r + 1):
                if i == m + 1:
                    nums[k] = tmp[j]
                    j += 1
                elif j == r + 1 or tmp[i] <= tmp[j]:
                    nums[k] = tmp[i]
                    i += 1
                else:
                    nums[k] = tmp[j]
                    j += 1
                    res += m - i + 1  # 统计逆序对
            return res

        tmp = [0] * len(nums)
        return merge_sort(0, len(nums) - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.reversePairs([7, 5, 6, 4]))
    # print(s.reversePairs([0]))
    # print(s.reversePairs([0,0]))
