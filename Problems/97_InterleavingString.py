from typing import Deque, List, Set, Tuple


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        m = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        m[0][0] = 1

        for row in range(len(s1) + 1):
            for col in range(len(s2) + 1):
                if row == col == 0:
                    continue
                if row == 0:
                    m[row][col] = 1 if m[row][col-1] == 1 and s3[col-1] == s2[col-1] else 0
                elif col == 0:
                    m[row][col] = 1 if m[row-1][col] == 1 and s3[row-1] == s1[row-1] else 0
                elif ((m[row-1][col] == 1 and s3[row+col-1] == s1[row-1])
                      or (m[row][col-1] == 1 and s3[row+col-1] == s2[col-1])):
                    m[row][col] = 1

        return m[len(s1)][len(s2)] != 0

    def isInterleave_3(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        to_check = Deque()
        to_check.append((0, 0))

        m: Set[Tuple[int, int]] = set()
        t3: int
        while to_check:
            t1, t2 = to_check.pop()
            t3 = t1 + t2
            if len(s1) == t1 and len(s2) == t2:
                return True
            if (t1, t2) in m:
                continue

            if len(s1) > t1 and s1[t1] == s3[t3]:
                to_check.append((t1+1, t2))

            if len(s2) > t2 and s2[t2] == s3[t3]:
                to_check.append((t1, t2+1))

            m.add((t1, t2))

        return False

    def isInterleave_2(self, s1: str, s2: str, s3: str) -> bool:

        to_check = Deque()
        to_check.append((0, 0, 0))

        m: Set[Tuple[int, int, int]] = set()

        while to_check:
            t1, t2, t3 = to_check.pop()
            if len(s1) == t1 and len(s2) == t2 and len(s3) == t3:
                return True
            if len(s1) == t1 and len(s2) == t2:
                continue
            if len(s3) == t3:
                continue
            if (t1, t2, t3) in m:
                continue

            if len(s1) > t1 and s1[t1] == s3[t3]:
                to_check.append((t1+1, t2, t3+1))

            if len(s2) > t2 and s2[t2] == s3[t3]:
                to_check.append((t1, t2+1, t3+1))

            m.add((t1, t2, t3))

        return False

    def isInterleave_1(self, s1: str, s2: str, s3: str) -> bool:

        to_check = Deque()
        to_check.append((s1, s2, s3))

        m: Set[Tuple[str, str, str]] = set()

        while to_check:
            t1, t2, t3 = to_check.pop()
            if len(t1) == len(t2) == len(t3) == 0:
                return True
            if len(t1) == len(t2) == 0:
                continue
            if len(t3) == 0:
                continue
            if (t1, t2, t3) in m:
                continue

            if len(t1) > 0 and t1[0] == t3[0]:
                to_check.append((t1[1:], t2, t3[1:]))

            if len(t2) > 0 and t2[0] == t3[0]:
                to_check.append((t1, t2[1:], t3[1:]))

            m.add((t1, t2, t3))

        return False


def do_test(i: int, s1: str, s2: str, s3: str, r):
    c = Solution()
    resp = c.isInterleave(s1, s2, s3)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "aabcc", "dbbca", "aadbbcbcac", True)
    do_test(1, "aabcc", "dbbca", "aadbbbaccc", False)
    do_test(2, "", "", "", True)
    do_test(3, "a", "b", "a", False)
    do_test(4, "", "b", "a", False)
    do_test(5, "a", "", "a", True)
    do_test(6, "a", "a", "aa", True)
    do_test(7, "aa", "", "aa", True)
    do_test(8, "aaaa", "aaab", "aaaabaaa", True)
    do_test(9, "abcd", "ef", "abcdef", True)
