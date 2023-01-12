from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        target = Counter(ransomNote)
        given = Counter(magazine)
        return len(target - given) == 0
    
    def canConstruct_2(self, ransomNote: str, magazine: str) -> bool:
        target = Counter()
        for c in ransomNote:
            target[c] += 1

        given = Counter()
        for c in magazine:
            given[c] += 1

        for k, v in target.items():
            if k not in given or given[k] < v:
                return False
        return True


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.canConstruct(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "a", "b", False)
    do_test(1, "aa", "ab", False)
    do_test(2, "aa", "aab", True)
