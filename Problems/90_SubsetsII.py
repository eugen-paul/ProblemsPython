from copy import deepcopy
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        resp = [[]]
        last_added_size = 0
        last_val = -100

        for current in nums:
            if last_val != current:
                size_before = len(resp)
                resp += [r + [current] for r in resp]
                last_added_size = len(resp) - size_before
            else:
                resp += [r + [current] for r in resp[len(resp) - last_added_size:]]
            last_val = current

        return resp

    def subsetsWithDup_3(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        resp = [[]]
        last_sub = [[]]
        last_val = -100

        for s in nums:
            if last_val != s:
                last_sub = [r + [s] for r in resp]
                resp.extend(deepcopy(last_sub))
            else:
                last_sub = [r + [s] for r in last_sub]
                resp.extend(deepcopy(last_sub))
            last_val = s

        return resp

    def subsetsWithDup_2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        resp = [[]]

        for s in nums:
            resp += [row + [s] for row in resp]

        return list(set(tuple(x) for x in resp))

    def subsetsWithDup_1(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        resp = [[]]

        for s in nums:
            resp += [row + [s] for row in resp]

        resp.sort()
        l = resp[-1]
        resp = [x for (x, y) in zip(resp, resp[1:]) if x != y]
        if resp[-1] != l:
            resp.append(l)
        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.subsetsWithDup(s)
    resp.sort()
    r.sort()
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
    do_test(1, [0], [[], [0]])
    do_test(2, [4, 4, 4, 1, 4], [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]])
    do_test(3, [1, 1], [[], [1], [1, 1]])
    do_test(4, [1, 1, 2, 2], [[], [1], [1, 1], [1, 1, 2], [1, 1, 2, 2], [1, 2], [1, 2, 2], [2], [2, 2]])
