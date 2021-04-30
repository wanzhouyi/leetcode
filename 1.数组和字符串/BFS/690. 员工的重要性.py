"""
给定一个保存员工信息的数据结构，它包含了员工 唯一的 id ，重要度和 直系下属的 id 。
比如，员工 1 是员工 2 的领导，员工 2 是员工 3 的领导。他们相应的重要度为 15 , 10 , 5 。那么员工 1 的数据结构是 [1, 15, [2]] ，员工 2的 数据结构是 [2, 10, [3]] ，员工 3 的数据结构是 [3, 5, []] 。注意虽然员工 3 也是员工 1 的一个下属，但是由于 并不是直系 下属，因此没有体现在员工 1 的数据结构中。
现在输入一个公司的所有员工信息，以及单个员工 id ，返回这个员工和他所有下属的重要度之和。

示例：
输入：[[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
输出：11
解释：
员工 1 自身的重要度是 5 ，他有两个直系下属 2 和 3 ，而且 2 和 3 的重要度均为 3 。因此员工 1 的总重要度是 5 + 3 + 3 = 11 。

提示：
一个员工最多有一个 直系 领导，但是可以有多个 直系 下属
员工数量不超过 2000 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/employee-importance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for Employee.
from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List[Employee], id: int) -> int:
        """
        方法一，暴力解法
        """
        ans = 0
        stack = [emp for emp in employees if emp.id == id]
        while stack:
            emp = stack.pop(0)
            ans += emp.importance
            stack.extend([who for who in employees if who.id in emp.subordinates])
        return ans

    def getImportance(self, employees: List[Employee], id: int) -> int:
        # BFS
        dic = dict()
        for emp in employees:
            dic[emp.id] = emp

        ans = 0
        stack = [dic[id]]
        while stack:
            emp = stack.pop(0)
            ans += emp.importance
            for sub in emp.subordinates:
                stack.append(dic[sub])
        return ans

    def getImportance(self, employees: List[Employee], id: int) -> int:
        # DFS
        dic = dict()
        for emp in employees:
            dic[emp.id] = emp
        ans = 0

        def dfs(emp: Employee):
            nonlocal ans
            ans += emp.importance
            for sub in emp.subordinates:
                dfs(dic[sub])

        dfs(dic[id])
