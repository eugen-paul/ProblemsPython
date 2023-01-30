from typing import List

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        l = [0,1,1]
        for _ in range(3,n+1):
            l.append(sum(l))
            l.pop(0)
        
        return l[2]
    
    def tribonacci_1(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        l1,l2,l3 = 0,1,1
        for _ in range(3,n+1):
            t = l1+l2+l3
            l1 = l2
            l2 = l3
            l3 = t
        
        return l3
        
def do_test(i: int, s, r):
    c = Solution()
    resp = c.tribonacci(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 0, 0)
    do_test(1, 1, 1)
    do_test(2, 2, 1)
    do_test(3, 3, 2)
    do_test(4, 4, 4)
    do_test(5, 5, 7)