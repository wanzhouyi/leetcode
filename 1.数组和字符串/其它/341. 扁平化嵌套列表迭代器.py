"""
给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。

列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。



示例 1:

输入: [[1,1],2,[1,1]]
输出: [1,1,2,1,1]
解释: 通过重复调用next 直到hasNext 返回 false，next返回的元素的顺序应该是: [1,1,2,1,1]。
示例 2:

输入: [1,[4,[6]]]
输出: [1,4,6]
解释: 通过重复调用next直到hasNext 返回 false，next返回的元素的顺序应该是: [1,4,6]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flatten-nested-list-iterator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import collections


class NestedIterator:
    def __init__(self, nestedList):
        self.arr = []

        def get_next(ls):
            for obj in ls:
                if isinstance(obj, list):
                    get_next(obj)
                else:
                    self.arr.append(obj)

        get_next(nestedList)

    def next(self) -> int:
        if self.hasNext():
            return self.arr.pop(0)

    def hasNext(self) -> bool:
        return self.arr != []


class NestedIterator(object):
    def dfs(self, nests):
        for nest in nests:
            if nest.isInteger():
                self.queue.append(nest.getInteger())
            else:
                self.dfs(nest.getList())

    def __init__(self, nestedList):
        self.queue = collections.deque()
        self.dfs(nestedList)

    def next(self):
        return self.queue.popleft()

    def hasNext(self):
        return len(self.queue)


class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = []
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])

    def next(self):
        cur = self.stack.pop()
        return cur.getInteger()

    def hasNext(self):
        while self.stack:
            cur = self.stack[-1]
            if cur.isInteger():
                return True
            self.stack.pop()
            for i in range(len(cur.getList()) - 1, -1, -1):
                self.stack.append(cur.getList()[i])
        return False


if __name__ == '__main__':
    s = NestedIterator([[1, 1], 2, [1, 1]])
    # s1=NestedIterator([1,[4,[6]]])
    while s.hasNext():
        print(s.next())
