'''
链接：https://www.nowcoder.com/questionTerminal/827e316ddc824cb6ac6825c1f720ed02?answerType=1&f=discussion
来源：牛客网

有一十进制正整数，移除其中的 K 个数，使剩下的数字是所有可能中最大的。
假设：
字符串的长度一定大于等于 K
字符串不会以 0 开头

输入描述:
一行由正整数组成的数字字符串，和一个正整数 K，两个数据用空格隔开，如：1432219 3。
字符串长度不超过2000，K<=2000。


输出描述:
移除 K 位后可能的最大的数字字符串。
如 1432219 移除 1, 2, 1 这 3 个数字后得到 4329，为所有可能中的最大值。
示例1
输入
1432219 3
输出
4329
'''


def func(s, K):
    k = int(K)
    stack = []

    for idx, num in enumerate(s):
        # 避免无效循环，K为0时退出
        if k == 0:
            break
        while stack and num > stack[-1] and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)

    result = (''.join(stack) + (s[idx + 1:] if idx == len(s) - 1 else s[idx:]))
    # 这里加了特判，有可能 k会大于0
    if k > 0:
        return result[:len(s) - int(K)]
    return result


if __name__ == '__main__':
    s, K = input().strip().split()
    print(func(s, K))
