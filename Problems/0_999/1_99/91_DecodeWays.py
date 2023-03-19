from typing import Deque, Dict, List, Set


class Solution:
    # number of ways to do something -> think about dp
    def numDecodings(self, s: str) -> int:
        """Internet solution"""
        # cannot map to any character due to the leading zero
        if s[0] == '0':
            return 0
        n = len(s)
        # dp[i]: number of ways of decoding the substring s[:i]
        dp = [0 for _ in range(n + 1)]
        # base case
        dp[0] = 1
        for i in range(1, n + 1):
            # check single digit decode
            # valid decode is possible only when s[i - 1] is not zero
            # if so, take the previous state dp[i - 1]
            # e.g. AB - 1[2]
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            # check double digit decode
            # by looking at the previous two digits
            # if the substring belongs to the range [10 - 26]
            # then add the previous state dp[i - 2]
            # e.g. L - [12]
            if i >= 2:
                # check the range
                if 10 <= int(s[i - 2: i]) <= 26:
                    dp[i] += dp[i - 2]
        return dp[n]
    
    def numDecodings_1(self, s: str) -> int:
        abc: Set[str] = {str(x) for x in range(1, 27)}

        m: Dict[str, int] = dict()

        def get_ways(sub: str) -> int:
            if sub == "":
                return 1

            if sub in m:
                return m[sub]

            count = 0
            one = sub[:1]
            if one in abc:
                count = get_ways(sub[1:])

            two = sub[:2]
            if two != "" and two != one and two in abc:
                count += get_ways(sub[2:])

            m[sub] = count

            return count

        return get_ways(s)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.numDecodings(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    # do_test(0, "12", 2)
    do_test(1, "226", 3)
    do_test(2, "06", 0)
    do_test(3, "1", 1)
    do_test(4, "10000", 0)
