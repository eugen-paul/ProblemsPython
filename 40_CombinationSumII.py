from typing import List


class Solution:
    def combinationSum2_sub(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0 or candidates[0] > target:
            return []

        resp = []

        last_number = -1
        for i, n in enumerate(candidates):
            rest = target - n
            if rest < 0:
                break
            if last_number == n:
                continue
            last_number = n
            if rest == 0:
                resp.append([n])
                return resp
            sub_resp = self.combinationSum2_sub(candidates[i+1:], rest)
            for sub_list in sub_resp:
                resp.append([n] + sub_list)

        if len(resp) > 0:
            return resp
        return []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.combinationSum2_sub(sorted(candidates), target)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.combinationSum2(s, n)

    resp = [sorted(x) for x in resp]
    r = [sorted(x) for x in r]

    if sorted(resp) == sorted(r):
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [10, 1, 2, 7, 6, 1, 5], 8, [
        [1, 1, 6],
        [1, 2, 5],
        [1, 7],
        [2, 6]
    ])

    do_test(1, [2, 5, 2, 1, 2], 5, [
        [1, 2, 2],
        [5]
    ])

    do_test(2, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 3, [
        [1, 1, 1]
    ])
