from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        """internet Solution"""
        # 3
        # 000
        # 001
        # 011
        # 010
        # 110
        # 111
        # 101
        # 100

        return [x ^ (x >> 1) for x in range(2**n)]

    def grayCode_1(self, n: int) -> List[int]:
        resp = [""] * (2**n)

        def set_bits(pos: int, bits: int, f: str, s: str):
            for i in range(bits // 2):
                resp[pos + i] += f

            if bits > 2:
                if f == "0":
                    set_bits(pos, bits // 2, f, s)
                else:
                    set_bits(pos, bits // 2, s, f)

            for i in range(bits // 2, bits):
                resp[pos + i] += s

            if bits > 2:
                if f == "1":
                    set_bits(pos + bits // 2, bits // 2, f, s)
                else:
                    set_bits(pos + bits // 2, bits // 2, s, f)

        set_bits(0, 2**n, "0", "1")

        return [int(x, base=2) for x in resp]


def do_test(i: int, s, r):
    c = Solution()
    resp = c.grayCode(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 2, [0, 1, 3, 2])
    do_test(1, 1, [0, 1])
    do_test(2, 3, [0, 1, 3, 2, 6, 7, 5, 4])
    do_test(3, 4, [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8])
