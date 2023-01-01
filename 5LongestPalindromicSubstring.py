class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        for i, c in enumerate(s):
            if len(s) - i <= len(longest):
                break

            for pos in range(len(s)-1, i-1, -1):
                if s[pos] != c:
                    continue
                l = pos - i + 1
                if l <= len(longest):
                    break
                t = s[i:pos+1]
                if t == t[::-1]:
                    longest = t
        return longest


if __name__ == "__main__":
    s = Solution()

    t1 = s.longestPalindrome("123456")
    if t1 == "1":
        print("OK 1")

    t1 = s.longestPalindrome("babad")
    if t1 == "bab" or t1 == "aba":
        print("OK 2")

    t1 = s.longestPalindrome("cbbd")
    if t1 == "bb":
        print("OK 3")
