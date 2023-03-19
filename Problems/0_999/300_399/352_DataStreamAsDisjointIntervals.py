from typing import List


class SummaryRanges:

    data: List[List[int]]

    def __init__(self):
        self.data = list()

    def addNum(self, value: int) -> None:
        """some ideas from solution"""
        l = 0
        r = len(self.data) - 1
        while l <= r:
            m = (l+r)//2
            if self.data[m][0] <= value <= self.data[m][1]:
                return
            elif value < self.data[m][0]:
                r = m-1
            else:
                l = m+1
        pos = l

        self.data.insert(pos, [value, value])
        if pos < len(self.data)-1 and self.data[pos+1][0] - 1 == value:
            self.data[pos: pos+2] = [[value, self.data[pos+1][1]]]

        if pos > 0 and self.data[pos-1][1] + 1 == value:
            self.data[pos-1: pos+1] = [[self.data[pos-1][0], self.data[pos][1]]]

    def addNum_1(self, value: int) -> None:
        new_self: List[List[int]] = list()
        current = [value, value]

        for interval in self.data:
            if interval[1] < current[0]-1:
                new_self.append(interval)
            elif current[1] < interval[0] - 1:
                new_self.append(current)
                current = interval
            else:
                current[0] = min(current[0], interval[0])
                current[1] = max(current[1], interval[1])

        new_self.append(current)
        self.data = new_self

    def getIntervals(self) -> List[List[int]]:
        return self.data


def do_test(i: int, s, n, r):
    c = SummaryRanges()
    for i in range(1, len(n)):
        if s[i] == "addNum":
            c.addNum(n[i][0])
        elif s[i] == "getIntervals":
            resp = c.getIntervals()
            if resp == r[i]:
                print("OK", i)
            else:
                print("NOK", i, "expected", r[i], "response", resp)


if __name__ == "__main__":
    do_test(0, ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"],
            [[], [1], [], [3], [], [7], [], [2], [], [6], []],
            [None, None, [[1, 1]], None, [[1, 1], [3, 3]], None, [[1, 1], [3, 3], [7, 7]], None, [[1, 3], [7, 7]], None, [[1, 3], [6, 7]]])
