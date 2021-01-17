"""
现在你总共有 n 门课需要选，记为0到n-1。

在选修某些课程之前需要一些先修课程。例如，想要学习课程 0 ，你需要先完成课程1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。

可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

示例1:

输入: 2, [[1,0]] 
输出: [0,1]
解释:总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
示例2:

输入: 4, [[1,0],[2,0],[3,1],[3,2]]
输出: [0,1,2,3] or [0,2,1,3]
解释:总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
    因此，一个正确的课程顺序是[0,1,2,3] 。另一个正确的排序是[0,2,1,3] 。
说明:

输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
提示:

这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
拓扑排序也可以通过BFS完成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，拓扑排序，288 ms，6.33%
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = dict()
        for i in range(numCourses):
            dic[i] = []
        for course in prerequisites:
            pre, post = course[1], course[0]
            dic[post].append(pre)
        # 找到没有依赖的节点
        stack = [x for x in dic.keys() if not dic[x]]
        ans = []
        while stack:
            course = stack.pop()
            ans.append(course)
            # 删除所有对它的依赖
            dictemp = dic.copy()
            for key, vals in dictemp.items():
                if course in vals:
                    dic[key].remove(course)
                    if not dic[key]:
                        dic.pop(key)
                        stack.append(key)
        if len(ans) < numCourses:
            return []
        return ans

    # 方法二，拓扑排序，空间换时间，40ms，97%
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        indegrees = defaultdict(int)
        edges = defaultdict(list)
        for i in range(numCourses):
            indegrees[i] = 0
        for prep in prerequisites:
            before = prep[1]
            after = prep[0]
            edges[before].append(after)
            indegrees[after] += 1
        result = []
        stack = [x[0] for x in indegrees.items() if x[1] == 0]
        while stack:
            course_bf = stack.pop(0)
            result.append(course_bf)
            for point in edges[course_bf]:
                indegrees[point] -= 1
                if indegrees[point] == 0:
                    stack.append(point)
        if len(result) < numCourses:
            return []
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.findOrder(2, [[1, 0]]))
    print(s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
