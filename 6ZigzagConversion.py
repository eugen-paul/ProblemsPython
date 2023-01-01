class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        down = True
        row = 0

        result = [[] for _ in range(numRows)]

        for c in s:
            result[row].append(c)
            if down:
                down = False if row == numRows - 1 else True
            else:
                down = True if row == 0 else False
            row = row + 1 if down else row - 1

        a = []
        for r in result:
            a.extend(r)
        return ''.join([str(elem) for elem in a])


if __name__ == "__main__":
    s = Solution()

    t1 = s.convert("PAYPALISHIRING", 3)
    if t1 == "PAHNAPLSIIGYIR":
        print("OK 1")

    t1 = s.convert("PAYPALISHIRING", 4)
    if t1 == "PINALSIGYAHRPI":
        print("OK 2")

    t1 = s.convert("A", 1)
    if t1 == "A":
        print("OK 3")

    t1 = s.convert("ABC", 1)
    if t1 == "ABC":
        print("OK 4")
