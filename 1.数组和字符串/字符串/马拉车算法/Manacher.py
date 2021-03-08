def manacher(s):
    assert '$' not in s and '^' not in s and '#' not in s
    if s == "":
        return (0, 1)
    t = "^#" + "#".join(s) + "#$"
    c = 0
    d = 0
    p = [0] * len(t)
    for i in range(1, len(t) - 1):
        # -- 相对于中心c 翻转下标i
        mirror = 2 * c - i  # = c - (i-c)
        p[i] = max(0, min(d - i, p[mirror]))  # -- 增加以i 为中心的回文子串的长度
        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1  # -- 必要时调整中心点
        if i + p[i] > d:
            c = i
            d = i + p[i]
    (k, i) = max((p[i], i) for i in range(1, len(t) - 1))
    return ((i - k) // 2, (i + k) // 2)  # 输出结果


if __name__ == '__main__':
    print(manacher("nonne"))
