"""
给你一个整数数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。

示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
示例 2：

输入：nums = [1], k = 1
输出：[1]
示例 3：

输入：nums = [1,-1], k = 1
输出：[1,-1]
示例 4：

输入：nums = [9,11], k = 2
输出：[11]
示例 5：

输入：nums = [4,-2], k = 2
输出：[4]


提示：

1 <= nums.length <= 105
-104<= nums[i] <= 104
1 <= k <= nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import bisect
import collections
import heapq
from typing import List


class Solution:
    # 超时
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        n = len(nums)
        window = sorted(nums[:k])
        ans = [window[-1]]
        for right in range(k, n):
            num_left = nums[left]
            num_left_index = bisect.bisect_left(window, num_left)
            # window.pop(num_left_index)
            del window[num_left_index]
            bisect.insort_left(window, nums[right])
            ans.append(window[-1])
            left += 1
        return ans


# 官解
# 前言
# 对于每个滑动窗口，我们可以使用 O(k)的时间遍历其中的每一个元素，找出其中的最大值。
# 对于长度为 n 的数组 nums 而言，窗口的数量为 n-k+1，因此该算法的时间复杂度为 O((n-k+1)k)=O(nk)，
# 会超出时间限制，因此我们需要进行一些优化。
#
# 我们可以想到，对于两个相邻（只差了一个位置）的滑动窗口，它们共用着 k-1 个元素，而只有 1 个元素是变化的。
# 我们可以根据这个特点进行优化。

class Solution:
    """
    方法一：优先队列
    思路与算法

    对于「最大值」，我们可以想到一种非常合适的数据结构，那就是优先队列（堆），其中的大根堆可以帮助我们实时维护一系列元素中的最大值。

    对于本题而言，初始时，我们将数组 nums 的前 k 个元素放入优先队列中。
    每当我们向右移动窗口时，我们就可以把一个新的元素放入优先队列中，此时堆顶的元素就是堆中所有元素的最大值。
    然而这个最大值可能并不在滑动窗口中，在这种情况下，这个值在数组nums 中的位置出现在滑动窗口左边界的左侧。
    因此，当我们后续继续向右移动窗口时，这个值就永远不可能出现在滑动窗口中了，我们可以将其永久地从优先队列中移除。

    我们不断地移除堆顶的元素，直到其确实出现在滑动窗口中。此时，堆顶元素就是滑动窗口中的最大值。
    为了方便判断堆顶元素与滑动窗口的位置关系，我们可以在优先队列中存储二元组 (num,index)，表示元素
    num 在数组中的下标为index。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/sliding-window-maximum/solution/hua-dong-chuang-kou-zui-da-zhi-by-leetco-ki6m/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans


class Solution:
    """
    方法二：单调队列
    思路与算法
    我们可以顺着方法一的思路继续进行优化。
    由于我们需要求出的是滑动窗口的最大值，如果当前的滑动窗口中有两个下标 i 和 j，其中 i 在 j 的左侧（i < j），
    并且 i 对应的元素不大于 j 对应的元素（nums[i]≤nums[j]），那么会发生什么呢？

    当滑动窗口向右移动时，只要 i 还在窗口中，那么 j 一定也还在窗口中，这是 i 在 j 的左侧所保证的。
    因此，由于 nums[j] 的存在，nums[i] 一定不会是滑动窗口中的最大值了，我们可以将 nums[i] 永久地移除。

    因此我们可以使用一个队列存储所有还没有被移除的下标。在队列中，这些下标按照从小到大的顺序被存储，
    并且它们在数组 nums 中对应的值是严格单调递减的。因为如果队列中有两个相邻的下标，它们对应的值相等或者递增，
    那么令前者为 i，后者为 j，就对应了上面所说的情况，即 nums[i] 会被移除，这就产生了矛盾。

    当滑动窗口向右移动时，我们需要把一个新的元素放入队列中。为了保持队列的性质，我们会不断地将新的元素与队尾的元素相比较，
    如果前者大于等于后者，那么队尾的元素就可以被永久地移除，我们将其弹出队列。
    我们需要不断地进行此项操作，直到队列为空或者新的元素小于队尾的元素。

    由于队列中下标对应的元素是严格单调递减的，因此此时队首下标对应的元素就是滑动窗口中的最大值。
    但与方法一中相同的是，此时的最大值可能在滑动窗口左边界的左侧，并且随着窗口向右移动，它永远不可能出现在滑动窗口中了。
    因此我们还需要不断从队首弹出元素，直到队首元素在窗口中为止。

    为了可以同时弹出队首和队尾的元素，我们需要使用双端队列。满足这种单调性的双端队列一般称作「单调队列」。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/sliding-window-maximum/solution/hua-dong-chuang-kou-zui-da-zhi-by-leetco-ki6m/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])

        return ans


class MonotonicQueue:
    """
    一、搭建解题框架
    这道题不复杂，难点在于如何在 O(1) 时间算出每个「窗口」中的最大值，使得整个算法在线性时间完成。
    在之前的文章【一个通用思想解决股票问题】中我们探讨过类似的场景，得到一个结论：

    在一堆数字中，已知最值，如果给这堆数添加一个数，那么比较一下就可以很快算出最值；但如果减少一个数，
    就不一定能很快得到最值了，而要遍历所有数重新找最值。
    回到这道题的场景，每个窗口前进的时候，要添加一个数同时减少一个数，
    所以想在 O(1) 的时间得出新的最值，就需要「单调队列」这种特殊的数据结构来辅助了。
    一个普通的队列一定有这两个操作：
    C++

    class Queue {
        void push(int n);
        // 或 enqueue，在队尾加入元素 n
        void pop();
        // 或 dequeue，删除队头元素
    }
    一个「单调队列」的操作也差不多：

    C++

    class MonotonicQueue {
        // 在队尾添加元素 n
        void push(int n);
        // 返回当前队列中的最大值
        int max();
        // 队头元素如果是 n，删除它
        void pop(int n);
    }
    当然，这几个 API 的实现方法肯定跟一般的 Queue 不一样，不过我们暂且不管，而且认为这几个操作的时间复杂度都是 O(1)，
    先把这道「滑动窗口」问题的解答框架搭出来：

    C++

    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        MonotonicQueue window;
        vector<int> res;
        for (int i = 0; i < nums.size(); i++) {
            if (i < k - 1) { //先把窗口的前 k - 1 填满
                window.push(nums[i]);
            } else { // 窗口开始向前滑动
                window.push(nums[i]);
                res.push_back(window.max());
                window.pop(nums[i - k + 1]);
                // nums[i - k + 1] 就是窗口最后的元素
            }
        }
        return res;
    }


    这个思路很简单，能理解吧？下面我们开始重头戏，单调队列的实现。

    二、实现单调队列数据结构
    首先我们要认识另一种数据结构：deque，即双端队列。很简单：

    C++

    class deque {
        // 在队头插入元素 n
        void push_front(int n);
        // 在队尾插入元素 n
        void push_back(int n);
        // 在队头删除元素
        void pop_front();
        // 在队尾删除元素
        void pop_back();
        // 返回队头元素
        int front();
        // 返回队尾元素
        int back();
    }
    而且，这些操作的复杂度都是 O(1)。这其实不是啥稀奇的数据结构，用链表作为底层结构的话，很容易实现这些功能。
    「单调队列」的核心思路和「单调栈」类似。单调队列的 push 方法依然在队尾添加元素，但是要把前面比新元素小的元素都删掉：

    C++

    class MonotonicQueue {
    private:
        deque<int> data;
    public:
        void push(int n) {
            while (!data.empty() && data.back() < n)
                data.pop_back();
            data.push_back(n);
        }
    };
    你可以想象，加入数字的大小代表人的体重，把前面体重不足的都压扁了，直到遇到更大的量级才停住。
    如果每个元素被加入时都这样操作，最终单调队列中的元素大小就会保持一个单调递减的顺序，因此我们的 max() API 可以可以这样写：

    C++

    int max() {
        return data.front();
    }
    pop() API 在队头删除元素 n，也很好写：

    C++

    void pop(int n) {
        if (!data.empty() && data.front() == n)
            data.pop_front();
    }
    之所以要判断 data.front() == n，是因为我们想删除的队头元素 n 可能已经被「压扁」了，这时候就不用删除了：

    至此，单调队列设计完毕，看下完整的解题代码：

    作者：labuladong
    链接：https://leetcode-cn.com/problems/sliding-window-maximum/solution/dan-diao-dui-lie-by-labuladong/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def __init__(self):
        self.win = []

    def win_push(self, a):
        while self.win and self.win[-1] < a:
            self.win.pop()
        self.win.append(a)

    def win_pop(self, a):
        if self.win and self.win[0] == a:
            self.win.pop(0)

    def win_max(self):
        return self.win[0]


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        if not nums or k == 0:
            return []
        n = len(nums)
        windows = MonotonicQueue()
        res = []
        for i in range(n):
            if i < k - 1:
                windows.win_push(nums[i])
            else:
                windows.win_push(nums[i])
                res.append(windows.win_max())
                windows.win_pop(nums[i - k + 1])
        return res


if __name__ == '__main__':
    s = Solution()
    # print(s.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
    print(s.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7, 2, 1, 0, -2, -3], k=3))
    # print(s.maxSlidingWindow(nums=[1], k=1))
    # print(s.maxSlidingWindow(nums=[1, -1], k=1))
    # print(s.maxSlidingWindow(nums=[9, 11], k=2))
    # print(s.maxSlidingWindow(nums=[4, -2], k=2))
    # import random
    #
    # nums = [random.randint(-10 ** 4, 10 ** 4) for _ in range(10 ** 5)]
    # print(s.maxSlidingWindow(nums, 55555))
