from typing import List


class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        nTol = [
            [" "],
            [],
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "i"],
            ["j", "k", "l"],
            ["m", "n", "o"],
            ["p", "q", "r", "s"],
            ["t", "u", "v"],
            ["w", "x", "y", "z"],
        ]

        response = []

        for c in digits:
            i = int(c)
            if len(response) == 0:
                response = response + nTol[i]
            else:
                n_res = []
                for n in nTol[i]:
                    n_res.extend([x+n for x in response])
                response = n_res

        return response

    def letterCombinations_dict(self, digits: str) -> List[str]:
        nTol = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
            "0": [" "],
        }

        response = []

        for c in digits:
            if len(response) == 0:
                response = response + nTol[c]
            else:
                n_res = []
                for n in nTol[c]:
                    n_res.extend([x+n for x in response])
                response = n_res

        return response


def do_test(i: int, s, r):
    c = Solution()
    resp = c.letterCombinations(s)
    if sorted(resp) == sorted(r):
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    do_test(1, "", [])
    do_test(2, "2", ["a", "b", "c"])
