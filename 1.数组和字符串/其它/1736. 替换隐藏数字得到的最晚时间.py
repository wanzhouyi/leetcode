"""
给你一个字符串 time ，格式为 hh:mm（小时：分钟），其中某几位数字被隐藏（用 ? 表示）。
有效的时间为 00:00 到 23:59 之间的所有时间，包括 00:00 和 23:59 。
替换time 中隐藏的数字，返回你可以得到的最晚有效时间。
示例 1：
输入：time = "2?:?0"
输出："23:50"
解释：以数字 '2' 开头的最晚一小时是 23 ，以 '0' 结尾的最晚一分钟是 50 。
示例 2：
输入：time = "0?:3?"
输出："09:39"
示例 3：
输入：time = "1?:22"
输出："19:22"
提示：
time 的格式为 hh:mm
题目数据保证你可以由输入的字符串生成有效的时间

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/latest-time-by-replacing-hidden-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    """
    方法一：贪心
    思路与算法

    为了得到最晚有效时间，我们可以从高位向低位枚举，在保证时间有效的情况下，使得每一位尽可能取最大值。

    因为本题中时间的位数较少，我们依次考虑每一位的规则即可。

    第一位：若第二位的值已经确定，且值落在区间 [4,9] 中时，第一位的值最大只能为 1，否则最大可以为 2；
    第二位：若第一位的值已经确定，且值为 2 时，第二位的值最大为 3，否则为 9；
    第三位：第三位的值的选取与其它位无关，最大为 5；
    第四位：第四位的值的选取与其它位无关，最大为 9。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/latest-time-by-replacing-hidden-digits/solution/ti-huan-yin-cang-shu-zi-de-dao-de-zui-wa-0s7r/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def maximumTime(self, time: str) -> str:
        arr = list(time)
        if arr[0] == '?':
            if arr[1] == '?' or int(arr[1]) <= 3:
                arr[0] = '2'
            else:
                arr[0] = '1'

        if arr[1] == '?':
            if arr[0] == '2':
                arr[1] = '3'
            else:
                arr[1] = '9'
        if arr[3] == '?':
            arr[3] = '5'
        if arr[4] == '?':
            arr[4] = '9'

        return ''.join(arr)


if __name__ == '__main__':
    s = Solution()
    print(s.maximumTime(time="2?:?0"))
    print(s.maximumTime(time="0?:3?"))
    print(s.maximumTime('??:??'))

    print(s.maximumTime(time="0?:33"))
    print(s.maximumTime(time="?0:33"))
    print(s.maximumTime(time="20:?3"))
    print(s.maximumTime(time="20:3?"))

    print(s.maximumTime(time="??:33"))
    print(s.maximumTime(time="?3:?3"))
    print(s.maximumTime(time="?3:3?"))

    print(s.maximumTime(time="1?:?3"))
    print(s.maximumTime(time="1?:3?"))
    print(s.maximumTime(time="13:??"))

    print(s.maximumTime("?4:03"))
