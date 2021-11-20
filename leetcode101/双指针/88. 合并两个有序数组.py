"""
给你两个按 非递减顺序 排列的整数数组nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，
其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。
示例 3：

输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
提示：

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109


进阶：你可以设计实现一个时间复杂度为 O(m + n) 的算法解决此问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[n:] = nums1[:m]
        print(nums1)
        x, y, pnt = n, 0, 0
        while x < m + n or y < n:
            if x < m + n and y < n:
                if nums1[x] <= nums2[y]:
                    nums1[pnt] = nums1[x]
                    x += 1
                    pnt += 1
                else:
                    nums1[pnt] = nums2[y]
                    y += 1
                    pnt += 1
            elif x < m + n and y == n:
                nums1[pnt] = nums1[x]
                x += 1
                pnt += 1
            elif y < n and x == m + n:
                nums1[pnt] = nums2[y]
                y += 1
                pnt += 1


"""
方法一：直接合并后排序
算法
最直观的方法是先将数组 nums_2放进数组 nums_1的尾部，然后直接对整个数组进行排序。
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()


"""
方法二：双指针
算法

方法一没有利用数组 nums_1与 nums_2已经被排序的性质。为了利用这一性质，我们可以使用双指针方法。
这一方法将两个数组看作队列，每次从两个数组头部取出比较小的数字放到结果中。如下面的动画所示：
我们为两个数组分别设置一个指针 p_1与 p_2来作为队列的头部指针。代码实现如下：
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                sorted.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorted.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                sorted.append(nums1[p1])
                p1 += 1
            else:
                sorted.append(nums2[p2])
                p2 += 1
        nums1[:] = sorted


"""
方法三：逆向双指针
算法
方法二中，之所以要使用临时变量，是因为如果直接合并到数组 nums_1中，nums_1中的元素可能会在取出之前被覆盖。
那么如何直接避免覆盖 nums_1中的元素呢？观察可知，nums_1的后半部分是空的，可以直接覆盖而不会影响结果。
因此可以指针设置为从后向前遍历，每次取两者之中的较大者放进 nums_1的最后面。
严格来说，在此遍历过程中的任意一个时刻，nums_1数组中有 m-p_1-1个元素被放入 nums_1的后半部，
nums_2数组中有 n-p_2-1个元素被放入 nums_1的后半部，而在指针 p_1的后面，nums_1数组有 m+n-p_1-1个位置。
由于m+n-p_1-1\geq m-p_1-1+n-p_2-1
m+n−p 
1
​
 −1≥m−p 
1
​
 −1+n−p 
2
​
 −1

等价于

p_2\geq -1
p 
2
​
 ≥−1

永远成立，因此 p_1p 
1
​
  后面的位置永远足够容纳被插入的元素，不会产生 p_1p 
1
​
  的元素被覆盖的情况。
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1


if __name__ == '__main__':
    s = Solution()
    print(s.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
    print(s.merge(nums1=[0], m=0, nums2=[1], n=1))
