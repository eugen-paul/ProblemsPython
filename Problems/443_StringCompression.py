from typing import List, Dict, Tuple, Counter


class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        last = chars[0]
        count = 1
        for c in chars[1:]:
            if c != last:
                s += last
                last = c
                if count != 1:
                    s += str(count)
                count = 1
            else:
                count += 1
        s += last
        if count != 1:
            s += str(count)
        for i, c in enumerate(s):
            chars[i] = c
        return len(s)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.compress(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, ["a", "a", "b", "b", "c", "c", "c"], 6)
    do_test(1, ["a"], 1)
    do_test(2, ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"], 4)
