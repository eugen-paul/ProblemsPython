from typing import Counter, List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # type of fruit
        f1, f2 = -1, -1
        # last position of fruit
        p1, p2 = -1, -1
        # start of currend window
        start = 0
        # maximum number of fruits
        max_len = 0

        for end, n in enumerate(fruits):
            #current fruit is a new fruit type and basket is full
            if f1 >= 0 and f2 >= 0 and f1 != n and f2 != n:
                #remove oldest fruit
                if p1 > p2:
                    start = p2+1
                    f2 = n
                else:
                    start = p1+1
                    f1 = n
            if f1 == -1 or f1 == n:
                f1 = n
                p1 = end
            else:
                f2 = n
                p2 = end
            max_len = max(end-start+1, max_len)

        return max_len

    def totalFruit_2(self, fruits: List[int]) -> int:
        c = Counter()
        l = 0
        max_len = 0

        for r, n in enumerate(fruits):
            if len(c) == 2 and n not in c:
                for lp in range(l, r):
                    c[fruits[lp]] -= 1
                    l += 1
                    if c[fruits[lp]] == 0:
                        del c[fruits[lp]]
                        break
            c[n] += 1
            max_len = max(c.total(), max_len)

        return max_len

    def totalFruit_1(self, fruits: List[int]) -> int:
        c = Counter()
        l = 0
        cur_len = 0
        max_len = 0

        for r, n in enumerate(fruits):
            if len(c) == 2 and n not in c:
                for lp in range(l, r):
                    cur_len -= 1
                    c[fruits[lp]] -= 1
                    l += 1
                    if c[fruits[lp]] == 0:
                        del c[fruits[lp]]
                        break
            c[n] += 1
            cur_len += 1
            max_len = max(cur_len, max_len)

        return max_len


def do_test(i: int, s, r):
    c = Solution()
    resp = c.totalFruit(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 1], 3)
    do_test(1, [0, 1, 2, 2], 3)
    do_test(2, [1, 2, 3, 2, 2], 4)
    do_test(3, [1, 2, 3, 2, 2, 1, 1, 1, 3], 5)
    do_test(4, [1, 2, 3], 2)
    do_test(5, [1], 1)
