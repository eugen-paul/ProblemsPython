from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pos = 0
        try:
            while True:
                c = strs[0][pos]

                for line in strs:
                    if line[pos] != c:
                        return strs[0][:pos]
                pos += 1
        except IndexError:
            return strs[0][:pos]
    
    def longestCommonPrefix_1(self, strs: List[str]) -> str:
        prefix = ""
        pos = 0
        while True:
            if len(strs[0]) <= pos:
                return prefix

            c = strs[0][pos]

            for line in strs:
                if len(line) <= pos or line[pos] != c:
                    return prefix
            prefix = prefix+c
            pos += 1


def do_test(i: int, s, r):
    c = Solution()
    resp = c.longestCommonPrefix(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, ["flower", "flow", "flight"], "fl")
    do_test(1, ["dog", "racecar", "car"], "")
    do_test(2, ["dog", "dogggiii", "d"], "d")
    do_test(3, ["dog"], "dog")
