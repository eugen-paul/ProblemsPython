from typing import List, Dict, Tuple, Counter


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        resp = [[1]]
        for r in range(1, numRows):
            sub = [1]
            for i in range(r-1):
                sub.append(resp[r-1][i] + resp[r-1][i+1])
            sub.append(1)
            resp.append(sub)
        return resp

    def generate_2(self, numRows: int) -> List[List[int]]:
        resp = [[1]]
        last_row = resp[0]
        for row in range(2, numRows + 1):
            r = [1]
            for i in range(1, row - 1):
                r.append(last_row[i - 1] + last_row[i])
            r.append(1)
            last_row = r
            resp.append(r)

        return resp

    def generate_1(self, numRows: int) -> List[List[int]]:
        resp = [[1]]

        for row in range(2, numRows + 1):
            r = []
            r.append(1)
            for i in range(1, row - 1):
                r.append(resp[row-2][i - 1] + resp[row-2][i])
            r.append(1)
            resp.append(r)

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.generate(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])
    do_test(1, 1, [[1]])
