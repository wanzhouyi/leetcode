"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
示例 1：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

提示：

1 <= nums.length <= 8
-10 <= nums[i] <= 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        def back_track(nums, path: list):
            if not nums:
                ans.add(tuple(path.copy()))
                return
            for i in range(len(nums)):
                path.append(nums[i])
                back_track(nums[:i] + nums[i + 1:], path)
                path.pop()

        back_track(nums, [])
        return list(map(list, ans))


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path.copy())
                return
            for i in range(size):
                if not used[i]:

                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue

                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth + 1, path, used, res)
                    used[i] = False
                    path.pop()

        size = len(nums)
        if size == 0:
            return []

        nums.sort()

        used = [False] * len(nums)
        res = []
        dfs(nums, size, 0, [], used, res)
        return res


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        ans = []
        n = len(nums)
        visited = [0] * n

        def dfs():
            if len(ans) == n:
                res.append(ans[::])
            for i in range(n):
                if visited[i] or i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:  # 关键代码
                    continue
                ans.append(nums[i])
                visited[i] = 1
                dfs()
                ans.pop()
                visited[i] = 0

        dfs()
        return res


class Solution:
    """
    看到 全排列，或者 枚举全部解，等类似的 搜索枚举类型题，基本就是 回溯 没跑了。
    因为回溯就是类似枚举的搜索尝试过程，主要是在搜索尝试过程中寻找问题的解，
    当发现已不满足求解条件时，就“回溯”返回，尝试别的路径。

    回溯主要的考虑的 三要素 已经在 46.全排列 写过了，但是这道题有了一点改变，那么就是列表里面有重复数字，
    全排列的结果，相同答案只算一种，那么我们就要优先考虑重复，再思考 三要素，定下我们思路和代码的基调。

    考虑重复
    重复即为：存在相同数字，比如 [1,2,2']，那么答案 [1,2,2'] 和 [1,2',2] 就其实是一样的，
    在保存结果的时候，我们只选择其一，但是这不是字符串，在保存结果的时候再去判断是否答案里已经保存了这一种情况会比较麻烦，
    那么我们能不能在生成答案的过程中就将其 剪枝（类比用过的数字就不考虑），这样根本就不会生成重复的答案了。

    我们希望的是，如果发现数字重复了，当前的就不考虑了，比如 [1,2,2'] 存在之后，当遇到 [1] 遇到 2'，发现和 2 重复了，
    我就直接剪枝，不考虑之后的所有的情况，因为：

        两个相同数字，我可以：
        两个都选
        两个都不选
        但是如果只选一个，那么选哪一个都可以，因为和选择另一个是相同情况，所以只有这种情况我们需要剪枝

    又到了小 trick 时间：
    考虑重复元素一定要优先排序，将重复的都放在一起，便于找到重复元素和剪枝！！！
    推广至 --> 如果涉及考虑重复元素，或者大小比较的情况，对列表排序是一个不错的选择

    好了，我们知道要排序，重复元素要剪枝，那么该如何剪枝呢？
    首先我们得使用第一个元素，因为这时候是第一次使用，还没有重复，并且所有情况都回溯搜索答案，
    除了用过的元素不再使用，其余不做剪枝，直到我们遇到第一个重复元素，我们才要考虑剪枝，
    但是考虑剪枝的时候还要考虑跟它重复的元素有没有被用过：

    如果前一个重复元素没有使用过，那么在当前重复元素下一层的可选项中一定会存在，也就是绿色部分
    那么一定会重复，即出现 2 X = X 2' 的情况（X为不选）
    也就是2和2' 以及 2'和2一定会重复，则整体剪枝，且是提前剪枝，在红色选择处就剪枝

    那么这部分剪枝的条件即为：和前一个元素值相同（此处隐含这个元素的index>0），并且前一个元素还没有被使用过

    回溯问题三要素
    把和 46.全排列 的区别--重复，考虑了之后，这道题就是和我们之前写过的思考过程一样了，依然是回到老三样：

    有效结果
    仍然是当前结果的长度==列表的长度，即为找到了一个有效结果

    if len(sol) == len(nums):
        self.res.append(sol)
    回溯范围及答案更新
    仍然是全部遍历，因为每一层都要考虑全部元素
    答案更新仍然是在修改 check 之后回溯内部累加更新 sol

    for i in range(len(nums)):
        check[i] = 1
        self.backtrack(sol+[nums[i]], nums, check)
        check[i] = 0
    剪枝条件
    在之前的 剪枝条件1：用过的元素不能再使用之外，又添加了一个新的剪枝条件，也就是我们考虑重复部分思考的结果，
    于是 剪枝条件2：当当前元素和前一个元素值相同（此处隐含这个元素的 index>0 ），并且前一个元素还没有被使用过的时候，我们要剪枝

    if check[i] == 1:
        continue
    if i > 0 and nums[i] == nums[i-1] and check[i-1] == 0:
        continue
    代码

    作者：sammy-4
    链接：https://leetcode-cn.com/problems/permutations-ii/solution/hot-100-47quan-pai-lie-ii-python3-hui-su-kao-lu-zh/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        check = [0 for i in range(len(nums))]

        self.backtrack([], nums, check)
        return self.res

    def backtrack(self, sol, nums, check):
        if len(sol) == len(nums):
            self.res.append(sol)
            return

        for i in range(len(nums)):
            if check[i] == 1:
                continue
            if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                continue
            check[i] = 1
            self.backtrack(sol + [nums[i]], nums, check)
            check[i] = 0


if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique(nums=[1, 1, 2]))
    print(s.permuteUnique(nums=[1, 2, 3]))
    print(s.permuteUnique(nums=[1]))
    print(s.permuteUnique(nums=[1, 1]))
    print(s.permuteUnique(nums=[1, 1, 1]))
