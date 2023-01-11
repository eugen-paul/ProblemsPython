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
            else:
                sub_resp = self.combinationSum(candidates[i:], rest)
                for sub_list in sub_resp:
                    resp.append([n] + sub_list)

        if len(resp) > 0:
            return resp
        return []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.combinationSum_sub(sorted(candidates), target)


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
    do_test(0, [2, 3, 6, 7], 7, [[2, 2, 3], [7]])
    do_test(1, [2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
    do_test(2, [2], 1, [])
    do_test(3, [8, 7, 4, 3], 11, [[8, 3], [7, 4], [4, 4, 3]])
