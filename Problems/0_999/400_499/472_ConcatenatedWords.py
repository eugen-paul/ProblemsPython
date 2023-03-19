from typing import Deque, List, Set


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """some help from solutions"""
        min_len = 50
        startchar_to_set: Set[str] = {*words}

        for w in words:
            min_len = min(min_len, len(w))

        resp = list()
        for w in words:
            if len(w) < min_len * 2:
                continue

            to_check: Deque[str] = Deque()
            to_check.append(w)

            is_ok = False
            while to_check:
                rest_word = to_check.pop()
                if len(rest_word) == 0:
                    is_ok = True
                    break

                for i in range(len(rest_word)):
                    sub_word = rest_word[:i+1]
                    if sub_word in startchar_to_set and w != sub_word:
                        to_check.append(rest_word[i+1:])

            if is_ok:
                resp.append(w)

        return resp

    def findAllConcatenatedWordsInADict_2(self, words: List[str]) -> List[str]:
        min_len = 50
        startchar_to_list: List[List[str]] = list()
        for _ in range(ord("z") - ord("a") + 1):
            startchar_to_list.append(list())

        for w in words:
            startchar_to_list[ord(w[0]) - ord("a")].append(w)
            min_len = min(min_len, len(w))

        for w in startchar_to_list:
            w.sort(key=len)

        resp = list()
        for w in words:
            if len(w) < min_len * 2:
                continue

            to_check: Deque[str] = Deque()
            to_check.append(w)

            is_ok = False
            while to_check:
                rest_word = to_check.pop()
                if len(rest_word) == 0:
                    is_ok = True
                    break

                for w_sm in startchar_to_list[ord(rest_word[0]) - ord("a")]:
                    if len(w_sm) > len(rest_word):
                        break
                    if rest_word.startswith(w_sm) and w != w_sm:
                        to_check.append(rest_word[len(w_sm):])

            if is_ok:
                resp.append(w)

        return resp

    def findAllConcatenatedWordsInADict_slow(self, words: List[str]) -> List[str]:
        """Slow but still fast enough. Very low memory."""
        startchar_to_list: List[List[str]] = list()
        for _ in range(ord("z") - ord("a") + 1):
            startchar_to_list.append(list())

        for w in words:
            startchar_to_list[ord(w[0]) - ord("a")].append(w)

        for w in startchar_to_list:
            w.sort(key=len)

        resp = list()
        for w in words:
            to_check: Deque[str] = Deque()
            to_check.append(w)

            is_ok = False
            while to_check:
                rest_word = to_check.pop()
                if len(rest_word) == 0:
                    is_ok = True
                    break

                for w_sm in startchar_to_list[ord(rest_word[0]) - ord("a")]:
                    if len(w_sm) > len(rest_word):
                        break
                    if rest_word.startswith(w_sm) and w != w_sm:
                        to_check.append(rest_word[len(w_sm):])

            if is_ok:
                resp.append(w)

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.findAllConcatenatedWordsInADict(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses",
            "rat", "ratcatdogcat"], ["catsdogcats", "dogcatsdog", "ratcatdogcat"])
    do_test(1, ["cat", "dog", "catdog"], ["catdog"])
