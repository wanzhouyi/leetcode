from typing import List


class clsA:
    @staticmethod
    def partial_table(p):
        '''''partial_table("ABCDABD") -> [0, 0, 0, 0, 1, 2, 0]'''
        prefix = set()
        res = [0]
        for i in range(1, len(p)):
            prefix.add(p[:i])
            postfix = {p[j:i + 1] for j in range(1, i + 1)}
            ls = list(prefix & postfix)
            if ls:
                ls.sort(key=lambda x: len(x), reverse=True)
                res.append(len(ls[0]))
            else:
                res.append(0)
        return res

    @staticmethod
    def kmp_match(s, p):
        m = len(s)
        n = len(p)
        cur = 0  # 起始指针cur
        table = clsA.partial_table(p)
        while cur <= m - n:  # 只去匹配前m-n个
            for i in range(n):
                if s[i + cur] != p[i]:
                    cur += max(i - table[i - 1], 1)  # 有了部分匹配表,我们不只是单纯的1位1位往右移,可以一次移动多位
                    break
            else:
                return True  # loop从 break 中退出时，else 部分不执行。
        return False


class clsB:
    # https: // blog.csdn.net / qq_42730750 / article / details / 108058105
    @staticmethod
    def getNext(substrT):
        next_list = [-1 for i in range(len(substrT))]
        j = 0
        t = -1
        while j < len(substrT) - 1:
            if t == -1 or substrT[j] == substrT[t]:
                j += 1
                t += 1
                # Tj=Tt, 则可以到的next[j+1]=t+1
                next_list[j] = t
            else:
                # Tj!=Tt, 模式串T索引为t的字符与当前位进行匹配
                t = next_list[t]
        return next_list


def KMP(substrS, substrT, next_list):
    count = 0
    j = 0
    t = 0
    while j < len(substrS) and t < len(substrT):
        if substrS[j] == substrT[t] or t == -1:
            # t == -1目的就是第一位匹配失败时
            # 主串位置加1, 匹配串回到第一个位置(索引为0)
            # 匹配成功, 主串和模式串指针都后移一位
            j += 1
            t += 1
        else:
            # 匹配失败, 模式串索引为t的字符与当前位进行比较
            count += 1
            t = next_list[t]
    if t == len(substrT):
        # 这里返回的是索引
        return j - t, count + 1
    else:
        return -1, count + 1


class clsC:
    # https://github.com/TheAlgorithms/Python/blob/master/strings/knuth_morris_pratt.py
    @staticmethod
    def get_failure_array(pattern: str) -> List[int]:
        """
        Calculates the new index we should go to if we fail a comparison
        :param pattern:
        :return:
        """
        failure = [0]
        i = 0
        j = 1
        while j < len(pattern):
            if pattern[i] == pattern[j]:
                i += 1
            elif i > 0:
                i = failure[i - 1]
                continue
            j += 1
            failure.append(i)
        return failure

    def kmp(pattern: str, text: str) -> bool:
        """
        The Knuth-Morris-Pratt Algorithm for finding a pattern within a piece of text
        with complexity O(n + m)
        1) Preprocess pattern to identify any suffixes that are identical to prefixes
            This tells us where to continue from if we get a mismatch between a character
            in our pattern and the text.
        2) Step through the text one character at a time and compare it to a character in
            the pattern updating our location within the pattern if necessary
        """

        # 1) Construct the failure array
        failure = clsC.get_failure_array(pattern)

        # 2) Step through text searching for pattern
        i, j = 0, 0  # index into text, pattern
        while i < len(text):
            if pattern[j] == text[i]:
                if j == (len(pattern) - 1):
                    return True
                j += 1

            # if this is a prefix in our pattern
            # just go back far enough to continue
            elif j > 0:
                j = failure[j - 1]
                continue
            i += 1
        return False


if __name__ == '__main__':
    # print(clsB.getNext("ABCDABD"))
    print(clsB.getNext("bbbbbbaa"))
