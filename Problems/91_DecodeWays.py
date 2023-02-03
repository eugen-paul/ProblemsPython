from typing import Deque, Dict, List, Set


class Solution:
    def numDecodings(self, s: str) -> int:
        abc: Set[str] = {str(x) for x in range(1, 27)}

        m: Dict[str, int] = dict()

        def get_ways(sub: str) -> int:
            if sub == "":
                return 1

            if sub in m:
                return m[sub]

            count = 0
            one = sub[:1]
            if one in abc:
                count = get_ways(sub[1:])

            two = sub[:2]
            if two != "" and two != one and two in abc:
                count += get_ways(sub[2:])

            m[sub] = count

            return count

        return get_ways(s)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.numDecodings(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "12", 2)
    do_test(1, "226", 3)
    do_test(2, "06", 0)
    do_test(3, "1", 1)
    do_test(4, "10000", 0)
