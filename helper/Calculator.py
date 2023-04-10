import re
from typing import Dict


def calc_1(s: str, prio: Dict[str, int]):
    """https://github.com/nb/advent/blob/master/2020/18.py"""
    i, values, ops = 0, [], []
    while i < len(s):
        if s[i] == ' ':
            i = i + 1
            continue
        elif s[i] == '(':
            ops.append(s[i])
        elif s[i].isdigit():
            n = re.match(r'^(\d+)', s[i:])[1]
            i = i + len(n) - 1
            values.append(int(n))
        elif s[i] == ')':
            while len(ops) != 0 and ops[-1] != '(':
                values.append(eval('%d%s%d' % (values.pop(), ops.pop(), values.pop())))
            ops.pop()  # (
        else:
            while len(ops) != 0 and prio[ops[-1]] >= prio[s[i]]:
                values.append(eval('%d%s%d' % (values.pop(), ops.pop(), values.pop())))
            ops.append(s[i])
        i = i + 1
    while len(ops) != 0:
        values.append(eval('%d%s%d' % (values.pop(), ops.pop(), values.pop())))
    return values[-1]


def calc_2(s: str):
    """!!! need space befor and after +/-/* !!!"""
    """https://github.com/LyndonFan/AdventOfCode/blob/main/2020/18.py"""
    s = s.strip()
    if not ("(" in s):
        splits = s.split(" ")  # <--- need space
        while "+" in splits:
            i = splits.index("+")
            splits[i-1] = str(int(splits[i-1]) + int(splits[i+1]))
            splits.pop(i)
            splits.pop(i)
        return eval(" ".join(splits))

    i = s.index("(")
    lvl = 1
    j = i+1
    while lvl > 0:
        lvl += s[j] == "("
        lvl -= s[j] == ")"
        j += 1
    newS = s[:i] + str(calc_2(s[i+1:j-1])) + s[j:]
    return calc_2(newS)


if __name__ == "__main__":
    prio = {'+': 1, '-': 1, '*': 1, '(': 0, ')': 0}
    print(calc_1("2*4+8", prio))
    prio = {'+': 2, '-': 2, '*': 1, '(': 0, ')': 0}
    print(calc_1("2*4+8", prio))

    print(calc_2("2 * 4 + 8"))
    print(calc_2("2 * (4 + 8)"))
