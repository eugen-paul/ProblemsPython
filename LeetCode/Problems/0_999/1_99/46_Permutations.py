from itertools import permutations
from typing import List


class Solution:
    # Heap's algorithm
    resp: list

    def heap_algo(self, k: int, A: List[int]):
        if k == 1:
            # output(A)
            self.resp.append(list(A))
        else:
            # Generate permutations with k-th unaltered
            # Initially k = length(A)
            self.heap_algo(k - 1, A)

            # Generate permutations for k-th swapped with each k-1 initial
            for i in range(k-1):
                # Swap choice dependent on parity of k (even or odd)
                if k % 2 == 0:
                    A[i], A[k-1] = A[k-1], A[i]
                else:
                    A[0], A[k-1] = A[k-1], A[0]
                self.heap_algo(k - 1, A)

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.resp = list()
        self.heap_algo(len(nums), nums)
        return self.resp

    def permute_simple(self, nums: List[int]) -> List[List[int]]:
        a = list(permutations(nums))
        return a


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def solve(sub: List[int]) -> List[List[int]]:
            if len(sub) <= 1:
                return [sub]

            resp = []
            pre = solve(sub[1:])
            for p in range(len(pre[0])+1):
                resp += [tmp[:p] + [sub[0]] + tmp[p:] for tmp in pre]
            return resp

        return solve(nums)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.permute(s)
    if sorted(resp) == sorted(r):
        print("OK", i)
    else:
        print("NOK", i, "expected", sorted(r), "response", sorted(resp))


if __name__ == "__main__":
    do_test(0, [1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
    do_test(1, [0, 1], [[0, 1], [1, 0]])
    do_test(2, [1], [[1]])
    do_test(3, [5, 4, 6, 2], [[5, 4, 6, 2], [5, 4, 2, 6], [5, 6, 4, 2], [5, 6, 2, 4], [5, 2, 4, 6], [5, 2, 6, 4], [4, 5, 6, 2], [4, 5, 2, 6], [4, 6, 5, 2], [4, 6, 2, 5], [4, 2, 5, 6], [
            4, 2, 6, 5], [6, 5, 4, 2], [6, 5, 2, 4], [6, 4, 5, 2], [6, 4, 2, 5], [6, 2, 5, 4], [6, 2, 4, 5], [2, 5, 4, 6], [2, 5, 6, 4], [2, 4, 5, 6], [2, 4, 6, 5], [2, 6, 5, 4], [2, 6, 4, 5]])
