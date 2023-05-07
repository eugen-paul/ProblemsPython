from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        dp = [-1 for _ in range(len(s))]

        def mem(start: int) -> int:
            if start == len(s):
                return 1
            if dp[start] == -1:
                if s[start] == "0":
                    dp[start] = 0
                else:
                    dp[start] = 0
                    for end in range(start+1, len(s)+1):
                        sub = int(s[start:end])
                        if sub > k:
                            break
                        else:
                            dp[start] = (dp[start] + mem(end)) % 1000000007

            return dp[start]

        return mem(0)
    
    def numberOfArrays_i(self, s: str, k: int) -> int:
        """sample solution"""
        m = len(s)
        mod = 10 ** 9 + 7
        
        # dp[i] records the number of arrays that can be printed as
        # the prefix substring s[0 ~ i - 1]
        dp = [1] + [0] * m
        
        # Iterate over every digit, for each digit s[start]:
        for start in range(m):
            if s[start] == '0':
                continue            
    
            # Iterate over ending digit end and find all valid numbers 
            # s[start ~ end].
            for end in range(start, m):  
                curr_number = s[start:end + 1]
                if int(curr_number) > k:
                    break
                
                # If s[start ~ end] is valid, increment dp[end + 1] by dp[start].
                dp[end + 1] += dp[start]
                dp[end + 1] %= mod
                    
        return dp[-1]


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.numberOfArrays(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "1000", 10000, 1)
    do_test(1, "1000", 10, 0)
    do_test(2, "1317", 2000, 8)
    do_test(3, "1234567890", 90, 34)
    do_test(4, "600342244431311113256628376226052681059918526204", 703, 411743991)
