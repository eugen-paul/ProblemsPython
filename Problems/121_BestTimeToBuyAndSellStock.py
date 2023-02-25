from typing import List, Dict, Tuple, Counter

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        cur = prices[0]
        
        for n in prices:
            cur = min(cur, n)
            best = max(best, n-cur)
        
        return best
    
    
def do_test(i: int, s, r):
    c = Solution()
    resp = c.maxProfit(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [7,1,5,3,6,4], 5)
    do_test(1, [7,6,4,3,1], 0)