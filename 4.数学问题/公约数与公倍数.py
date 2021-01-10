# 求最大公约数，使用辗转相除法（greatest common divisor，gcd）
# 将两个数相乘再除以最大公因数即可得到最小公倍数（least common multiple, lcm）。

# 方法一，使用math.gcd
import math

print(math.gcd(48, 60))


# 方法二，使用递归
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(48, 60))


# 求最小公倍数
def lcm(a, b):
    return a * b / gcd(a, b)


print(lcm(48, 60))
