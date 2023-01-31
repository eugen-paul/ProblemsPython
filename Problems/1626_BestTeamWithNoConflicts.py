from bisect import bisect_right
from typing import Deque, Dict, List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        ages_scores = list(zip(ages, scores))
        ages_scores.sort()

        m: Dict[(int), int] = dict()

        def get_max(pos: int) -> int:
            if (pos) in m:
                return m[pos]

            max_sc = ages_scores[pos][1]

            ag = ages_scores[pos][0]
            sc = max_sc

            for i in range(pos+1, len(ages_scores)):
                if ages_scores[i][0] == ag or ages_scores[i][1] >= sc:
                    max_sc = max(max_sc, sc + get_max(i))

            m[pos] = max_sc

            return max_sc

        sc = 0
        for i in range(len(ages_scores)):
            sc = max(sc, get_max(i))

        return sc

    def bestTeamScore_i1(self, scores, ages):
        """internet Solution"""
        dp = [0]*(max(ages)+1)

        for score, age in sorted(zip(scores, ages)):
            dp[age] = max(dp[:age+1]) + score

        return max(dp)

    def bestTeamScore_i1(self, scores, ages):
        """internet Solution"""
        new_list = sorted(zip(ages, scores))
        visited = [new_list[0][1]]
        dp = [new_list[0][1]]
        ans = new_list[0][1]

        for i in range(1, len(new_list)):
            s = new_list[i][1]
            index = bisect_right(visited, s)
            curr = max(dp[:index]) + s if index else s
            ans = max(ans, curr)
            visited.insert(index, s)
            dp.insert(index, curr)
        return ans

    def bestTeamScore_1(self, scores: List[int], ages: List[int]) -> int:
        ages_scores = list(zip(ages, scores))
        ages_scores.sort()

        m: Dict[(int, int, int), int] = dict()

        def get_max(pos: int, ag: int, sc: int) -> int:
            if pos >= len(ages_scores):
                return 0

            if (pos, ag, sc) in m:
                return m[(pos, ag, sc)]

            max_sc = 0

            for i in range(pos, len(ages_scores)):
                if ages_scores[i][0] == ag or ages_scores[i][1] >= sc:
                    max_sc = max(max_sc, ages_scores[i][1] + get_max(i+1, ages_scores[i][0], ages_scores[i][1]))

            m[(pos, ag, sc)] = max_sc

            return max_sc

        sc = get_max(0, 0, 0)

        return sc


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.bestTeamScore(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    # do_test(0, [1, 3, 5, 10, 15], [1, 2, 3, 4, 5], 34)
    # do_test(1, [4, 5, 6, 5], [2, 1, 2, 1], 16)
    # do_test(2, [1, 2, 3, 5], [8, 9, 10, 1], 6)
    # do_test(3, [2], [1], 2)
    # do_test(4, [1, 2, 3], [1, 1, 1], 6)
    do_test(4, [3, 2, 1], [1, 1, 1], 6)
    do_test(5, [3, 3, 3], [1, 2, 3], 9)
    do_test(6, [4, 2, 3, 4, 5], [1, 2, 3, 4, 5], 14)
    do_test(7, [1, 15, 3, 4, 5], [1, 2, 3, 4, 5], 16)
    do_test(8, [1, 6, 3, 4, 5], [1, 2, 3, 4, 5], 13)
    do_test(9, [10, 2, 3, 4, 10], [1, 2, 3, 4, 5], 20)
