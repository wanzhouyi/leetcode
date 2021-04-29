"""
一只青蛙想要过河。 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。
青蛙可以跳上石子，但是不可以跳入水中。
给你石子的位置列表 stones（用单元格序号 升序 表示），请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。
开始时，青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格 1 跳至单元格 2 ）。
如果青蛙上一步跳跃了k个单位，那么它接下来的跳跃距离只能选择为k - 1、k或k + 1 个单位。
另请注意，青蛙只能向前方（终点的方向）跳跃。

示例 1：
输入：stones = [0,1,3,5,6,8,12,17]
输出：true
解释：青蛙可以成功过河，按照如下方案跳跃：跳 1 个单位到第 2 块石子, 然后跳 2 个单位到第 3 块石子, 接着 跳 2 个单位到第 4 块石子, 然后跳 3 个单位到第 6 块石子, 跳 4 个单位到第 7 块石子, 最后，跳 5 个单位到第 8 个石子（即最后一块石子）。

示例 2：
输入：stones = [0,1,2,3,4,8,9,11]
输出：false
解释：这是因为第 5 和第 6 个石子之间的间距太大，没有可选的方案供青蛙跳跃过去。

提示：

2 <= stones.length <= 2000
0 <= stones[i] <= 231 - 1
stones[0] == 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/frog-jump
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import defaultdict
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # 如果第二步与第一步之间距离大于1，说明无法跳到第二步
        if stones[1] > 1:
            return False
        # 初始化一个集合类型的字典，并设置第二步为1。集合里的数字代表跳到当前石头需要多少个跳跃单位。
        dic = defaultdict(set)
        dic[1] = {1}
        # 为减少循环次数，只遍历有小石头的格子
        for num in stones[1:]:
            # 计算从当前格子能够跳到的格子
            for step in dic[num].copy():
                dic[num + step - 1].add(step - 1)
                dic[num + step].add(step)
                dic[num + step + 1].add(step + 1)
        # 最后检查，最后一个格子是否有能够跳入的可能
        if len(dic[stones[-1]]) > 0:
            return True
        return False
