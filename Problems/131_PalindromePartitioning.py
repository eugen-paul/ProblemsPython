from typing import Dict, List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        buf: Dict[str, List[List[str]]] = dict()

        def get_subs(sub_s: str) -> List[List[str]]:
            if len(sub_s) == 0:
                return [[]]

            if len(sub_s) == 1:
                return [[sub_s]]

            if sub_s in buf:
                return buf[sub_s]

            current_subs = list()

            for i in range(len(sub_s)):
                subsub = sub_s[:i+1]
                if subsub == subsub[::-1]:
                    current_subs.extend([[subsub] + x for x in get_subs(sub_s[i+1:])])

            buf[sub_s] = current_subs

            return current_subs

        return get_subs(s)

    def partition_slow(self, s: str) -> List[List[str]]:
        resp = list()

        current_pol = list()

        def get_subs(sub_s: str):
            if len(sub_s) == 0:
                resp.append(current_pol.copy())
                return

            for i in range(len(sub_s)):
                subsub = sub_s[:i+1]
                if subsub == subsub[::-1]:
                    current_pol.append(subsub)
                    get_subs(sub_s[i+1:])
                    current_pol.pop()

        get_subs(s)

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.partition(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "aab", [["a", "a", "b"], ["aa", "b"]])
    do_test(1, "a", [["a"]])
    do_test(2, "aa", [["a", "a"], ["aa"]])
