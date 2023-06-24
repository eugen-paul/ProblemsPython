from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        self.resp = 0
        m = {}

        def comp(pos: int, a: int, b: int) -> int:
            if (pos, a-b) in m:
                return m[(pos, a-b)]

            if pos >= len(rods):
                if a == b:
                    return 0
                return -1

            resp = -1
            tmp = comp(pos+1, a, b)
            if tmp >= 0:
                resp = tmp

            cur = rods[pos]
            tmp = comp(pos+1, a+cur, b)
            if tmp >= 0:
                resp = max(resp, tmp + cur)

            tmp = comp(pos+1, a, b+cur)
            if tmp >= 0:
                resp = max(resp, tmp)

            m[(pos, a-b)] = resp
            return resp

        return comp(0, 0, 0)

    def tallestBillboard_s1(self, rods):
        """sample solution"""
        # Helper function to collect every combination `(left, right)`
        def helper(half_rods):
            states = set()
            states.add((0, 0))
            for r in half_rods:
                new_states = set()
                for left, right in states:
                    new_states.add((left + r, right))
                    new_states.add((left, right + r))
                states |= new_states

            dp = {}
            for left, right in states:
                dp[left - right] = max(dp.get(left - right, 0), left)
            return dp

        n = len(rods)
        first_half = helper(rods[:n // 2])
        second_half = helper(rods[n // 2:])

        answer = 0
        for diff in first_half:
            if -diff in second_half:
                answer = max(answer, first_half[diff] + second_half[-diff])
        return answer

    def tallestBillboard_s2(self, rods: List[int]) -> int:
        """sample solution"""
        # dp[taller - shorter] = taller
        dp = {0:0}
        
        for r in rods:
            # dp.copy() means we don't add r to these stands.
            new_dp = dp.copy()
            for diff, taller in dp.items():
                shorter = taller - diff
                
                # Add r to the taller stand, thus the height difference is increased to diff + r.
                new_dp[diff + r] = max(new_dp.get(diff + r, 0), taller + r)
                
                # Add r to the shorter stand, the height difference is expressed as abs(shorter + r - taller).
                new_diff = abs(shorter + r - taller)
                new_taller = max(shorter + r, taller)
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), new_taller)
                
            dp = new_dp
            
        # Return the maximum height with 0 difference.
        return dp.get(0, 0)

def do_test(i: int, s, r):
    c = Solution()
    resp = c.tallestBillboard(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 6], 6)
    do_test(1, [1, 2, 3, 4, 5, 6], 10)
    do_test(2, [1, 2], 0)
    do_test(3, [1, 1], 1)
    do_test(4, [1, 1, 1, 1], 2)
    do_test(5, [1, 1, 2], 2)
    do_test(6, [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 50, 50, 50, 150, 150, 150, 100, 100, 100, 123], 1023)
