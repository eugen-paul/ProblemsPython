from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        resp = list()
        intervals.sort()

        current = intervals[0]
        for i in intervals:
            if current[1] < i[0]:
                resp.append(current)
                current = i
                continue

            if current[1] >= i[1]:
                continue

            current[1] = i[1]

        resp.append(current)

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.merge(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]])
    do_test(1, [[1, 4], [4, 5]], [[1, 5]])
    do_test(2, [[1, 4], [2, 3]], [[1, 4]])
    do_test(3, [[1, 4], [6, 7]], [[1, 4], [6, 7]])
    do_test(4, [[1, 4], [1, 4]], [[1, 4]])
    do_test(5, [[6, 7], [1, 4]], [[1, 4], [6, 7]])
