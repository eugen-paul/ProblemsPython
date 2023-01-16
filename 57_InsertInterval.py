from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        resp = []

        state = 0

        current = newInterval
        for p in intervals:
            if state == 0:
                if p[1] < current[0]:
                    resp.append(p)
                elif current[1] < p[0]:
                    resp.append(current)
                    resp.append(p)
                    state = 1
                else:
                    current = [min(p[0], current[0]), max(p[1], current[1])]
            else:
                resp.append(p)

        if state == 0:
            resp.append(current)

        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.insert(s, n)
    resp.sort()
    r.sort()
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]])
    do_test(1, [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]])
    do_test(2, [[3, 5]], [1, 1], [[1, 1], [3, 5]])
    do_test(3, [[3, 5]], [7, 8], [[3, 5], [7, 8]])
    do_test(4, [[3, 5]], [6, 8], [[3, 5], [6, 8]])
