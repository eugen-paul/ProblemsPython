from itertools import permutations
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = set(permutations(nums))
        return [list(x) for x in perms]

    def permuteUnique_simple(self, nums: List[int]) -> List[List[int]]:
        return list(set(permutations(nums)))


def do_test(i: int, s, r):
    c = Solution()
    resp = c.permuteUnique(s)
    if sorted(resp) == sorted(r):
        print("OK", i)
    else:
        print("NOK", i, "expected", sorted(r), "response", sorted(resp))


if __name__ == "__main__":
    do_test(0, [1, 1, 2], [
        [1, 1, 2],
        [1, 2, 1],
        [2, 1, 1]
    ])
    do_test(1, [1, 2, 3], [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ])
