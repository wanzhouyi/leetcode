"""
你这个学期必须选修 numCourses 门课程，记为0到numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组prerequisites 给出，其中prerequisites[i] = [ai, bi] ，表示如果要学习课程ai 则 必须 先学习课程 bi 。

例如，先修课程对[0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

示例 1：

输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
示例 2：

输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。

提示：

1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
prerequisites[i] 中的所有课程对 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic_edges = defaultdict(list)
        dic_degree = dict()
        for course in range(numCourses):
            dic_edges[course] = []  # 依赖的课程
            dic_degree[course] = 0  # 入度

        for pre in prerequisites:
            dic_edges[pre[1]].append(pre[0])
            dic_degree[pre[0]] += 1
        zero_nodes = [item[0] for item in dic_degree.items() if item[1] == 0]
        while zero_nodes:
            zero = zero_nodes.pop(0)
            dic_degree.pop(zero)

            for ic in dic_edges[zero]:
                dic_degree[ic] -= 1
                if dic_degree[ic] == 0:
                    zero_nodes.append(ic)
        if len(dic_degree) > 0:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(numCourses=2, prerequisites=[[1, 0]]))
    print(s.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))
