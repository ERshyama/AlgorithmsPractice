# Author: Shyama Arunachalam


def mul(x, n):
    multiple, step = 1, 1
    value_dict = {1: (x, 1)}
    num, expo = x, 1

    while expo <= n:
        num = num + num
        step = step + 1
        expo = expo + expo
        value_dict[step] = (num, expo)

    remaining = n
    answer = 0
    while remaining > 0:
        val, power = value_dict[step]
        if power > remaining:
            step = step - 1
            continue
        answer = answer + val
        remaining = remaining - power
        step = step - 1

    return answer


x = 2.10000
n = 3
ans = mul(x, n)
print(ans)
