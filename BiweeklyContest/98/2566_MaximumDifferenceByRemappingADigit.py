from typing import List, Dict, Tuple, Counter


class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        min_v = 10_000_000_000
        max_v = 0

        for i in range(10):
            min_v = min(int(s.replace(str(i), "0")), min_v)
            max_v = max(int(s.replace(str(i), "9")), max_v)

        return int(max_v) - int(min_v)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.minMaxDifference(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 11891, 99009)
    do_test(1, 90, 99)
