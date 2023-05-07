import math
from typing import List, Dict, Tuple, Counter


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        resp = list()

        fr = math.factorial(rowIndex)
        for i in range(rowIndex+1):
            resp += [fr // (math.factorial(i) * math.factorial(rowIndex-i))]

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.getRow(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 3, [1, 3, 3, 1])
    do_test(1, 0, [1])
    do_test(2, 1, [1, 1])
    do_test(3, 4, [1, 4, 6, 4, 1])
    do_test(4, 5, [1, 5, 10, 10, 5, 1])
