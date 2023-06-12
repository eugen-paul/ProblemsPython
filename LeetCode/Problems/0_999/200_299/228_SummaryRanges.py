from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        last = nums[0]
        cur_start = last
        resp = []
        for i in range(1, len(nums)):
            if last+1 != nums[i]:
                if cur_start == last:
                    resp.append(str(last))
                else:
                    resp.append(str(cur_start)+"->"+str(last))
                cur_start = nums[i]
            last = nums[i]

        if last+1 != nums[i]:
            if cur_start == last:
                resp.append(str(last))
            else:
                resp.append(str(cur_start)+"->"+str(last))

        return resp

    def summaryRanges_s(self, nums: List[int]) -> List[str]:
        """sample solution"""
        ranges = []     
        i = 0 
        
        while i < len(nums): 
            start = nums[i]  
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]: 
                i += 1 
            
            if start != nums[i]: 
                ranges.append(str(start) + "->" + str(nums[i]))
            else: 
                ranges.append(str(nums[i]))
            
            i += 1

        return ranges

def do_test(i: int, s, r):
    c = Solution()
    resp = c.summaryRanges(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"])
    do_test(1, [0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"])
    do_test(2, [0], ["0"])
    do_test(3, [], [])
    do_test(4, [1, 2, 3], ["1->3"])
    do_test(5, [-1], ["-1"])
    do_test(6, [-10, -4, -3, -2, 1, 2], ["-10", "-4->-2", "1->2"])
