from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        resp = [[]]

        for n in nums:
            resp += [x + [n] for x in resp]

        return resp

    def subsets_1(self, nums: List[int]) -> List[List[int]]:
        resp = [[nums.pop(0)]]

        while nums:
            n = nums.pop(0)
            resp += [[n]]
            resp += [x + [n] for x in resp if n not in x]

        resp.append([])
        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.subsets(s)
    resp.sort()
    r.sort()
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
    do_test(1, [0], [[], [0]])
