from typing import List


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [None] * (n+1)
        dp[0] = 1

        def get_rest(c: int) -> int:
            if dp[c]:
                return dp[c]

            resp = 0
            for i in range(1, c+1):
                resp += get_rest(i-1) * get_rest(c-i)

            dp[c] = resp
            return resp

        return get_rest(n)

    def numTrees_1(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            for r in range(1, i + 1):
                dp[i] += dp[r - 1] * dp[i - r]

        return dp[n]


def do_test(i: int, s, r):
    c = Solution()
    resp = c.numTrees(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 3, 5)
    do_test(1, 1, 1)
    do_test(2, 2, 2)
