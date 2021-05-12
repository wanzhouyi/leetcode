"""
给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。
请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。
工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。
返回分配方案中尽可能 最小 的 最大工作时间 。


示例 1：

输入：jobs = [3,2,3], k = 3
输出：3
解释：给每位工人分配一项工作，最大工作时间是 3 。
示例 2：

输入：jobs = [1,2,4,7,8], k = 2
输出：11
解释：按下述方式分配工作：
1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
2 号工人：4、7（工作时间 = 4 + 7 = 11）
最大工作时间是 11 。

提示：

1 <= k <= jobs.length <= 12
1 <= jobs[i] <= 107

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        """
        失败！
        方法一，拿到这个题第一想法是贪心。思路大概是这样的。

        if k == 1:
            return sum(jobs)
        elif k == 2:
            # 分成两堆，尽可能平均。先取最大的，然后依次取小的，哪堆小就放哪堆
            pass
        elif k == 3:
            # 分成三堆，尽可能平均。先取最大的，然后依次取小的，哪堆小就放哪堆
            pass

        但是这样只能通过48/60的用例，卡在这种情况下
        jobs=[5,5,4,4,4],k=2。
        """
        workers = [0] * k
        jobs.sort()
        while jobs:
            job = jobs.pop()
            min_worker = min(workers)
            idx = workers.index(min_worker)
            workers[idx] += job
        return max(workers)

    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        """
        失败！
        方法二，看到数据规模是12，但是k和n都是12，可能会超过10**7，抱着侥幸心理用DFS试一下

        果然不出所料，超时了，用例通过率是16/60，卡在这个用例上
        [9899456,8291115,9477657,9288480,5146275,7697968,8573153,3582365,3758448,9881935,2420271,4542202]，9
        """
        job_asign = [0] * k
        n = len(jobs)
        ans = float('inf')

        def dfs(job, job_asign):
            if job == n:
                nonlocal ans
                ans = min(ans, max(job_asign))
                return

            for i in range(k):
                job_asign[i] += jobs[job]
                dfs(job + 1, job_asign)
                job_asign[i] -= jobs[job]

        dfs(0, job_asign)
        return ans

    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        """
       失败！
       方法三，在方法二的基础上用了lru_cache，但还是超时了，用例通过率是43/60，卡在这个用例上
        [254,256,256,254,251,256,254,253,255,251,251,255]，10
        """

        job_asign = (0,) * k
        n = len(jobs)
        ans = float('inf')

        from functools import lru_cache
        @lru_cache
        def dfs(job, job_asign_param):
            job_asign = list(job_asign_param)
            if job == n:
                nonlocal ans
                ans = min(ans, max(job_asign))
                return

            for i in range(k):
                job_asign[i] += jobs[job]
                dfs(job + 1, tuple(sorted(job_asign)))
                job_asign[i] -= jobs[job]

        dfs(0, tuple(job_asign))
        return ans

    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        """
       失败！
       方法四，方法三用了lru_cache，但还是超时了。原因是什么呢，其实只是减少了部分运算量，能不能继续减少呢
        """

        job_asign = (0,) * k
        n = len(jobs)
        ans = float('inf')

        from functools import lru_cache
        @lru_cache
        def dfs(job, job_asign_param):
            job_asign = list(job_asign_param)
            if job == n:
                nonlocal ans
                ans = min(ans, max(job_asign))
                return
            # // 优先分配给「空闲工人」
            if 0 in job_asign:
                idx = job_asign.index(0)
                job_asign[idx] += jobs[job]
                dfs(job + 1, tuple(sorted(job_asign)))
                job_asign[idx] -= jobs[job]

            for i in range(k):
                job_asign[i] += jobs[job]
                dfs(job + 1, tuple(sorted(job_asign)))
                job_asign[i] -= jobs[job]

        dfs(0, tuple(job_asign))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minimumTimeRequired(jobs=[3, 2, 3], k=3))
    print(s.minimumTimeRequired(jobs=[1, 2, 4, 7, 8], k=2))
    print(s.minimumTimeRequired(jobs=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], k=12))
    print(s.minimumTimeRequired([5, 5, 4, 4, 4], 2))  # 这个用例导致排序+贪心算法行不通
