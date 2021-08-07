"""
有两个长度相同的字符串s1 和s2，且它们其中只含有字符"x" 和"y"，你需要通过「交换字符」的方式使这两个字符串相同。
每次「交换字符」的时候，你都可以在两个字符串中各选一个字符进行交换。
交换只能发生在两个不同的字符串之间，绝对不能发生在同一个字符串内部。
也就是说，我们可以交换s1[i] 和s2[j]，但不能交换s1[i] 和s1[j]。
最后，请你返回使 s1 和 s2 相同的最小交换次数，如果没有方法能够使得这两个字符串相同，则返回-1 。

示例 1：
输入：s1 = "xx", s2 = "yy"
输出：1
解释：
交换 s1[0] 和 s2[1]，得到 s1 = "yx"，s2 = "yx"。

示例 2：
输入：s1 = "xy", s2 = "yx"
输出：2
解释：
交换 s1[0] 和 s2[0]，得到 s1 = "yy"，s2 = "xx" 。
交换 s1[0] 和 s2[1]，得到 s1 = "xy"，s2 = "xy" 。
注意，你不能交换 s1[0] 和 s1[1] 使得 s1 变成 "yx"，因为我们只能交换属于两个不同字符串的字符。

示例 3：
输入：s1 = "xx", s2 = "xy"
输出：-1
示例 4：

输入：s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
输出：4

提示：

1 <= s1.length, s2.length <= 1000
s1, s2只包含'x'或'y'。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-swaps-to-make-strings-equal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    """
    这道题写出答案很短，但是逻辑推断需要耐心。解决这道题，首先有一条定理需要留意：
    字符的交换仅仅出现在存在不同字符的位置。例如“xxxy”和“xyxx”这两个字符串，第一个位置和第三个位置是相同的，
    我们可以把这些相同的位置去除，实际上把这两个字符串输入到函数中，与把“xy”和“yx”（只保留第二个位置和第四个位置）输入到函数中，
    函数输出的数字是完全一样的。

    因此，我们实际上只需要管那些在两个字符串中不同的位置，用数组diff记录下这些位置处第一个字符串s1的字符，
    列表推导式就可以快速得到：diff = [c1 for c1, c2 in zip(s1, s2) if c1 != c2]，为什么不用s2的了呢？
    因为有了s1的，s2的按照s1的各个位置翻转一下就有了。

    首先，如diff中有奇数个字符，说明s1与s2有奇数个位置不同，换来换去最后一定会有一个s1或s2中某个位置不一样，
    一定无法满足条件，读者可以自行尝试；

    如果s1与s2不同的位置有偶数个，就要看这些不同位置中“x”或“y”的个数是奇是偶。看diff就够了，
    如果diff中“x”的个数有偶数个（隐含着“y”的个数也有偶数个），对于这些不同的位置，可以两两完成交换，
    一次交换可以满足两个位置的相同，那么交换的次数是len(diff)//2，
    例如“xxxxyy”与“yyyyxx”，我们可以分成三组，“xx”和“yy”，“xx”和“yy”，“yy”和“xx”，组内对角位置交换就够了，
    注意这里为了便于表示“x”和“y”分别在左右两边，因此只需要交换3次即可，也就是。

    如果diff中“x”的个数有奇数个（隐含着“y”的个数也有奇数个），例如“xxxyyy”和“yyyxxxx”，可
    以分成三组，“xx”和“yy”，“xy”和“yx”（既然“x”个数是奇数个，这种情况一定会存在的），“yy”和“xx”，
    需要的交换次数为1+2+1=4，也就是len(diff)//2+1，这里多出来的1实际上就是“xy”和“yx”这种情况造成的，
    要先对应位置交换，再对角交换，比其他情况多了一步。

    作者：skx
    链接：https://leetcode-cn.com/problems/minimum-swaps-to-make-strings-equal/solution/luo-ji-tui-li-fen-lei-tao-lun-ti-si-lu-q-06g0/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def minimumSwap(self, s1: str, s2: str) -> int:
        diff = [c1 for c1, c2 in zip(s1, s2) if c1 != c2]
        if len(diff) % 2 == 1:
            return -1
        if diff.count("x") % 2 == 0:
            return len(diff) // 2
        return len(diff) // 2 + 1


if __name__ == '__main__':
    s = Solution()
    print(s.minimumSwap(s1="xx", s2="yy"))
