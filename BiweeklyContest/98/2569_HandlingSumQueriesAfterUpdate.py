from typing import List, Dict, Tuple, Counter


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        """better but still too slow"""
        count_1 = sum(nums1)
        sum_2 = sum(nums2)

        resp = list()
        for q in queries:
            if q[0] == 1:
                for i in range(q[1], q[2]+1):
                    if nums1[i] == 0:
                        nums1[i] = 1
                        count_1 += 1
                    else:
                        nums1[i] = 0
                        count_1 -= 1
            elif q[0] == 2:
                sum_2 += count_1 * q[1]
            else:
                resp.append(sum_2)

        return resp

    def handleQuery_1(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        """too slow"""
        resp = list()
        for q in queries:
            if q[0] == 1:
                for i in range(q[1], q[2]+1):
                    if nums1[i] == 0:
                        nums1[i] = 1
                    else:
                        nums1[i] = 0
            elif q[0] == 2:
                nums2 = [a*q[1] + b for a, b in zip(nums1, nums2)]
            else:
                resp.append(sum(nums2))

        return resp


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.handleQuery(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0,  [1, 0, 1], [0, 0, 0], [[1, 1, 1], [2, 1, 0], [3, 0, 0]], [3])
    do_test(1,  [1], [5], [[2, 0, 0], [3, 0, 0]], [5])
