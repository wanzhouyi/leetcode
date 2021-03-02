# http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html
def partial_table(p):
    '''''partial_table("ABCDABD") -> [0, 0, 0, 0, 1, 2, 0]'''
    prefix = set()
    res = [0]
    for i in range(1, len(p)):
        prefix.add(p[:i])
        postfix = {p[j:i + 1] for j in range(1, i + 1)}
        # print(p[:i+1],prefix,postfix,prefix & postfix or {''})
        res.append(len((prefix & postfix or {''}).pop()))
    return res


def kmp_match(s, p):
    m = len(s)
    n = len(p)
    cur = 0  # 起始指针cur
    table = partial_table(p)
    while cur <= m - n:  # 只去匹配前m-n个
        for i in range(n):
            if s[i + cur] != p[i]:
                cur += max(i - table[i - 1], 1)  # 有了部分匹配表,我们不只是单纯的1位1位往右移,可以一次移动多位
                break
        else:
            return True  # loop从 break 中退出时，else 部分不执行。
    return False


if __name__ == '__main__':
    # print(partial_table("ABCDABD"))
    print(kmp_match("BBC ABCDAB ABCDABCDABDE", "ABCDABD"))
