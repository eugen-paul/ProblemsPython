from collections import Counter
from typing import Dict, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resp_dict: Dict[str, List[str]] = dict()

        for w in strs:
            ws_re = "".join(sorted(list(w)))
            if ws_re in resp_dict:
                resp_dict[ws_re].append(w)
            else:
                resp_dict[ws_re] = [w]

        return [x for x in resp_dict.values()]

    def groupAnagrams_2(self, strs: List[str]) -> List[List[str]]:
        resp_dict: Dict[str, List[str]] = dict()

        def count_chars(s: str) -> List[int]:
            count = [0] * 26
            for c in s:
                count[ord(c)-97] += 1
            return count

        for w in strs:
            ws = count_chars(w)
            ws_re = ws.__repr__()
            d = resp_dict.get(ws_re, None)
            if d is None:
                resp_dict[ws_re] = [w]
            else:
                d.append(w)

        return [x for x in resp_dict.values()]

    def groupAnagrams_3(self, strs: List[str]) -> List[List[str]]:
        resp = list()
        resp_dict = dict()

        for w in strs:
            ws = Counter(sorted(w))
            d = resp_dict.get(ws.__repr__(), None)
            if d is None:
                n = list()
                n.append(w)
                resp_dict[ws.__repr__()] = list(n)
            else:
                d.append(w)

        for _, v, in resp_dict.items():
            resp.append(v)

        return resp

    def groupAnagrams_slow_2(self, strs: List[str]) -> List[List[str]]:
        resp_dict = list()

        for w in strs:
            ws = Counter(w)
            found = False
            for c in resp_dict:
                if c[0] == ws:
                    c[1].append(w)
                    found = True
                    break
            if not found:
                resp_dict.append((ws, [w]))

        return [x[1] for x in resp_dict]

    def groupAnagrams_slow(self, strs: List[str]) -> List[List[str]]:
        resp = list()

        for w in strs:
            ws = Counter(w)
            is_new = True
            for a in resp:
                is_found = False
                for c in a:
                    cs = Counter(c)
                    if ws == cs:
                        is_new = False
                        is_found = True
                        a.append(w)
                        break
                if is_found:
                    break
            if is_new:
                n = list()
                n.append(w)
                resp.append(n)

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.groupAnagrams(s)
    for x in resp:
        x.sort()
    resp.sort()
    for x in r:
        x.sort()
    r.sort()
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, ["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    do_test(1, [""], [[""]])
    do_test(2, ["a"], [["a"]])
