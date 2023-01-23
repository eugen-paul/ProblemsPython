import math
from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        When moving through the labyrinth, the whole path from the robot consists exactly of m-1 steps down and n-1 steps right. The steps can occur in any order. 
        The path is exactly m-1+n-1 steps long. Use the probability to calculate the lottery wins to determine the number of all possible paths (Binomial coefficient).
        """
        if m == 1 or n == 1:
            return 1

        m = m - 1
        n = n - 1

        if n > m:
            n, m = m, n

        n_m = m+n
        resp = math.factorial(n_m) // (math.factorial(n) * math.factorial(n_m-n))

        return min(resp, 2 * 10**9)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.uniquePaths(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 3, 7, 28)
    do_test(1, 3, 2, 3)
