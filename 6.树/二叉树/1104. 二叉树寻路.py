"""
在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按“之” 字形进行标记。
如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；
而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。
给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。
示例 1：
输入：label = 14
输出：[1,3,4,14]
示例 2：
输入：label = 26
输出：[1,2,6,10,26]

提示：

1 <= label <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-in-zigzag-labelled-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # 计算最大层数
        import math
        max_level = math.ceil(math.log2(10 ** 6))
        level = -1
        for i in range(max_level):
            if 2 ** i <= label < 2 ** (i + 1):
                level = i
                break
        ans = []
        var = label
        while level >= 0:
            ans.insert(0, var)
            if level % 2 == 0:
                index = var - 2 ** level
                parent_index = index // 2
                var = 2 ** level - 1 - parent_index

            else:
                index = 2 ** (level + 1) - 1 - var
                parent_index = index // 2
                var = 2 ** (level - 1) + parent_index
            level -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.pathInZigZagTree(14))
    print(s.pathInZigZagTree(26))
    print(s.pathInZigZagTree(10 ** 6))
