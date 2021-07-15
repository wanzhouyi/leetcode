"""
给你一个正整数数组arr。请你对 arr执行一些操作（也可以不进行任何操作），使得数组满足以下条件：
arr中 第一个元素必须为1。
任意相邻两个元素的差的绝对值 小于等于1，
也就是说，对于任意的 1 <= i < arr.length（数组下标从 0 开始），都满足abs(arr[i] - arr[i - 1]) <= 1。
abs(x)为x的绝对值。
你可以执行以下 2 种操作任意次：

减小 arr中任意元素的值，使其变为一个 更小的正整数。
重新排列arr中的元素，你可以以任意顺序重新排列。
请你返回执行以上操作后，在满足前文所述的条件下，arr中可能的 最大值。

示例 1：
输入：arr = [2,2,1,2,1]
输出：2
解释：
我们可以重新排列 arr 得到 [1,2,2,2,1] ，该数组满足所有条件。
arr 中最大元素为 2 。

示例 2：
输入：arr = [100,1,1000]
输出：3
解释：
一个可行的方案如下：
1. 重新排列 arr 得到 [1,100,1000] 。
2. 将第二个元素减小为 2 。
3. 将第三个元素减小为 3 。
现在 arr = [1,2,3] ，满足所有条件。
arr 中最大元素为 3 。

示例 3：
输入：arr = [1,2,3,4,5]
输出：5
解释：数组已经满足所有条件，最大元素为 5 。

提示：

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-element-after-decreasing-and-rearranging
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        if arr[0] > 1:
            arr[0] = 1

        n = len(arr)
        for i in range(1, n):
            if abs(arr[i] - arr[i - 1]) > 1:
                arr[i] = arr[i - 1] + 1
        return arr[-1]


# ----------解
class Solution:
    """
    排序+贪心
    由于数组差值绝对值不超过1，换而言之，数组中相邻两个数要么相等，要么相差1，
    理想的情况下，数组最后会变成 [1,2,……,n] 的顺序排列，但并不是任何时候都能得到理想的情况，
    因为题目限制我们只能对数组中的数做减小操作而不能增大，所以我们可以贪心的将小的数字尽量放前面

    那么为什么这种做法是正确的呢？

    首先，我们考虑数组和 sum(arr)，在能执行的两种操作中，重排数组不会对数组的和产生影响，
    而减小数组中的值会使得数组和减小，那么当数组元素取得最大值时，数组和也会取得最大值


    结论：贪心的取得最小值执行减小操作使得数组和最大
    不难得到，因为减小元素的操作会使数组和变小，所以要使数组和尽量大，那么我们要使减小元素的操作减少得尽量少，
    例如，在数组的第一个位置，我们取数组中最小的值，将其减小到 1 ，可以使得数组和减少的尽量少，
    由上面的证明可知，数组和尽量大即数组最大值尽量大

     一般的，我们先对数组排序，对于第 i 个位置，我们最理想的取值是比第 i - 1 位置的值大 1，
     所以我们在位置 i 及后面的数中取最小的那个，将其减小到比第 i - 1 位置的值大1，
     不过若是取得最小的数与第 i - 1 位置的数相同或仅大1，那么就不执行减小操作（因为数组已经排序，
     所以位置 i 及后面的数不可能小于第 i- 1 位置的数）


    作者：meteordream
    链接：https://leetcode-cn.com/problems/maximum-element-after-decreasing-and-rearranging/solution/jian-xiao-he-zhong-xin-pai-lie-shu-zu-ho-sv8z/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        """排序+贪心"""
        n = len(arr)
        arr.sort()
        arr[0] = 1
        for i in range(1, n):
            if arr[i] - arr[i - 1] > 1:
                arr[i] = arr[i - 1] + 1
        return arr[n - 1]


class Solution:
    """
    计数排序
    前面提到过，数组成 [1,2,……,n] 的顺序排列是最理想的情况，但却不一定实现，原因是我们只能将大值缩小而不能将小的数字增大，例如有 n 个 1 组成的数组那最大只能是 1

    我们可以考虑这样一种做法：将数组中的值往这个理想情况填空，若我们能填满所有位置，那就是理想情况了，最大值为 n ，若出现一些位置无法填到,那么就要将后面大的数字缩小后用于填充

    具体实现时，大于n的值都缩小为 n ，然后我们由后往前遍历统计数组，若某位置存在重复值，那么多出来的数字可以用于缩小填充前面不存在值的位置，若某位置不存在值且没有更大的数缩小填充，那就只能将后面的所有数字都前移一位，当然不用真的移动，只需记录下需要前移的次数即可，举个栗子： [1, 2, 9, 8, 1]

    计数结果为 [2, 1, 0, 0, 2] 分别代表 1 ~ 5
    在5 的位置有两个数，可以取 1 个数用于前面的填充
    在4 位置没有值，需要用 5 填充，此时数组为 [2, 1, 0, 1, 1]
    在3 位置没有值，也没有可用于填充的数字, 只能将后面的 4,5 前移： [2, 1, 1, 1, 0]
    在2,1 位置都有值无需前移，所以最后结果就是 n - 前移次数，即 4

    作者：meteordream
    链接：https://leetcode-cn.com/problems/maximum-element-after-decreasing-and-rearranging/solution/jian-xiao-he-zhong-xin-pai-lie-shu-zu-ho-sv8z/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        """计数排序"""
        n = len(arr)
        s = [0 for _ in range(n + 1)]
        for a in arr:
            if a > n:
                s[n] += 1
            else:
                s[a] += 1
        cnt, k = 0, 0
        for i in range(n, 0, -1):
            if s[i] != 0:
                k += s[i] - 1
            elif k != 0:
                k -= 1
            else:
                cnt += 1
        return n - cnt
