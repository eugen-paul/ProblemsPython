from typing import List


class Solution:

    def combinationSum_sub(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0 or candidates[0] > target:
            return []

        resp = []

        for i, n in enumerate(candidates):
            rest = target - n
            if rest < 0:
                break
            if rest == 0:
                resp.append([n])
                return resp
            sub_resp = self.combinationSum_sub(candidates[i:], rest)
            for sub_list in sub_resp:
                resp.append([n] + sub_list)

        if len(resp) > 0:
            return resp
        return []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.combinationSum_sub(sorted(candidates), target)

    def combinationSum_ways_2(self, target: int) -> int:
        """ways to get target from [1,3,5]"""
        dp = [0] * (target + 1)
        dp[0] = 1

        for sub_target in range(1, target+1):
            dp[sub_target] = dp[sub_target - 1]

            if sub_target >= 3:
                dp[sub_target] += dp[sub_target - 3]
            if sub_target >= 5:
                dp[sub_target] += dp[sub_target - 5]

        return dp[target]

    def combinationSum_ways_1(self, target: int) -> int:
        """ways to get target from [1,3,5]"""
        dp = [None] * (target + 1)

        def get_n(sub_target: int) -> int:
            if sub_target < 0:
                return 0
            if sub_target == 0:
                return 1

            if dp[sub_target]:
                return dp[sub_target]

            dp[sub_target] = get_n(sub_target-1) + get_n(sub_target-3) + get_n(sub_target-5)
            return dp[sub_target]

        return get_n(target)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.combinationSum(s, n)

    resp = [sorted(x) for x in resp]
    r = [sorted(x) for x in r]

    if sorted(resp) == sorted(r):
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    c = Solution()
    print(c.combinationSum_ways_1(1), c.combinationSum_ways_2(1))
    print(c.combinationSum_ways_1(2), c.combinationSum_ways_2(2))
    print(c.combinationSum_ways_1(3), c.combinationSum_ways_2(3))
    print(c.combinationSum_ways_1(4), c.combinationSum_ways_2(4))
    print(c.combinationSum_ways_1(5), c.combinationSum_ways_2(5))
    print(c.combinationSum_ways_1(6), c.combinationSum_ways_2(6))
    print(c.combinationSum_ways_1(7), c.combinationSum_ways_2(7))
    print(c.combinationSum_ways_1(8), c.combinationSum_ways_2(8))

    do_test(0, [2, 3, 6, 7], 7, [[2, 2, 3], [7]])
    do_test(1, [2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
    do_test(2, [2], 1, [])
    do_test(3, [8, 7, 4, 3], 11, [[8, 3], [7, 4], [4, 4, 3]])
