"""
给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。

有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。



示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：

输入：s = "0000"
输出：["0.0.0.0"]
示例 3：

输入：s = "1111"
输出：["1.1.1.1"]
示例 4：

输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]
示例 5：

输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


提示：

0 <= s.length <= 3000
s 仅由数字组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-ip-addresses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        n = len(s)

        def back_track(start: int, index: int, path: list):
            if index == 4:
                if start == n:
                    ans.append('.'.join(path))
                return
            for i in range(1, 4):
                ipsec = s[start:start + i]
                if len(ipsec) > 0 and (
                        i == 1 or (i > 1 and not ipsec.startswith('0') and int(ipsec) < 256)):
                    path.append(s[start:start + i])
                    back_track(start + i, index + 1, path)
                    path.pop()

        back_track(0, 0, [])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses(s="25525511135"))
    print(s.restoreIpAddresses(s="0000"))
    print(s.restoreIpAddresses(s='1111'))
    print(s.restoreIpAddresses(s="010010"))
    print(s.restoreIpAddresses(s="101023"))
