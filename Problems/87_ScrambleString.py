from typing import Counter, Dict, List, Tuple


class Solution:
    m: Dict[Tuple[str, str], bool] = dict()

    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        if (s1, s2) in self.m:
            return self.m[(s1, s2)]

        c_l1 = Counter()
        c_r1 = Counter(s1)

        c_l2 = Counter()
        c_r2 = Counter(s2)

        c_l3 = Counter(s2)
        c_r3 = Counter()
        for i in range(1, len(s1)):
            left1 = s1[:i]
            right1 = s1[i:]
            c_l1[left1[-1]] += 1
            c_r1[left1[-1]] -= 1

            left2 = s2[:i]
            right2 = s2[i:]
            c_l2[left2[-1]] += 1
            c_r2[left2[-1]] -= 1

            if c_l1 == c_l2 and c_r1 == c_r2 and self.isScramble(left1, left2) and self.isScramble(right1, right2):
                self.m[(s1, s2)] = True
                return True

            left3 = s2[:len(s2)-i]
            right3 = s2[len(s2)-i:]
            c_l3[right3[0]] -= 1
            c_r3[right3[0]] += 1

            if c_l1 == c_r3 and c_r1 == c_l3 and self.isScramble(left1, right3) and self.isScramble(right1, left3):
                self.m[(s1, s2)] = True
                return True

        self.m[(s1, s2)] = False
        return False

    def isScramble_1(self, s1: str, s2: str) -> bool:
        """ok, but slow"""
        if s1 == s2:
            return True

        if (s1, s2) in self.m:
            return self.m[(s1, s2)]

        for i in range(1, len(s1)):
            left1, right1 = s1[:i], s1[i:]
            left2, right2 = s2[:i], s2[i:]

            if self.isScramble(left1, left2) and self.isScramble(right1, right2):
                self.m[(s1, s2)] = True
                return True

            left3, right3 = s2[:len(s2)-i], s2[len(s2)-i:]

            if self.isScramble(left1, right3) and self.isScramble(right1, left3):
                self.m[(s1, s2)] = True
                return True

        self.m[(s1, s2)] = False
        return False


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.isScramble(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "great", "rgeat", True)
    do_test(1, "abcde", "caebd", False)
    do_test(2, "a", "a", True)
    do_test(3, "abcd", "cbcd", False)
    do_test(4, "eebaacbcbcadaaedceaaacadccd", "eadcaacabaddaceacbceaabeccd", False)
