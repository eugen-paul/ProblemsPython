from typing import List, Dict, Tuple, Counter


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        s = set(nums)
        resp = 0

        while s:
            n = s.pop()
            p = n+1
            count = 1
            while p in s:
                count += 1
                s.remove(p)
                p += 1
            p = n-1
            while p in s:
                count += 1
                s.remove(p)
                p -= 1
            resp = max(resp, count)

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.longestConsecutive(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [100, 4, 200, 1, 3, 2], 4)
    do_test(1, [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9)
    do_test(2, [10, 11, 12, 1], 3)
    do_test(3, [1, 4, 6, 1], 1)
    do_test(4, [-1, 0, 1, -2, -3, 10, 11], 5)
