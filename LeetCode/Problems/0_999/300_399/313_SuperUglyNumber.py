from collections import defaultdict
from functools import cache
import heapq
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ma = 2**32
        if n == 1:
            return 1
        q = primes.copy()
        s = set(primes)
        heapq.heapify(q)
        cur = 1
        while cur != n-1:
            mi = heapq.heappop(q)
            for p in primes:
                tmp = p*mi
                if tmp <= ma and tmp not in s:
                    s.add(tmp)
                    heapq.heappush(q, tmp)
                elif tmp > ma:
                    break
            cur += 1
        return q[0]

    def nthSuperUglyNumber_i(self, n: int, primes: List[int]) -> int:
        """internet solution"""
        # create a list to store the super ugly numbers, initialize with 1
        super_ugly = [1]
        # create a list to store the indices for each prime number
        idx = [0] * len(primes)
        # create a list to store the product of prime numbers with their corresponding indices
        # this will be used to find the next super ugly number
        prod = [p for p in primes]

        # loop until we find the nth super ugly number
        while len(super_ugly) < n:
            # find the minimum value in prod, which will be the next super ugly number
            next_ugly = min(prod)
            # append it to the list of super ugly numbers
            super_ugly.append(next_ugly)

            # update the index for each prime number whose product is equal to next_ugly
            for i in range(len(primes)):
                if next_ugly == prod[i]:
                    idx[i] += 1
                    prod[i] = primes[i] * super_ugly[idx[i]]

        # return the last element in the list of super ugly numbers, which is the nth super ugly number
        return super_ugly[-1]

    def nthSuperUglyNumber_i(self, n: int, primes: List[int]) -> int:
        """internet solution"""
        nums = primes.copy()  # do a deep copy
        heapq.heapify(nums)  # create a heap
        p = 1
        for i in range(n - 1):
            p = heapq.heappop(nums)  # take the smallest element
            for prime in primes:
                heapq.heappush(nums, p * prime)  # add all those multiples with the smallest number
                if p % prime == 0:
                    break
        return p


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.nthSuperUglyNumber(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 12, [2, 7, 13, 19], 32)
    do_test(1, 1,  [2, 3, 5], 1)


def get_nb(x: int, y: int, maxX: int, maxY: int, minX: int = 0, minY: int = 0, dia: bool = False) -> List[Tuple[int, int]]:
    resp = []

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if dia:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        xn, yn = x+dx, y+dy
        if minX <= xn <= maxX and minY <= yn <= maxY:
            resp.append((xn, yn))
    return resp
