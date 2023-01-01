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

    def longest_palindrome_expand(self, s: str) -> str:
        longest = s[0]

        def expand(p1, p2):
            if (p2 >= len(s)) or s[p1] != s[p2]:
                return ""

            while 0 < p1 <= p2 <= len(s)-2 and s[p1-1] == s[p2+1]:
                p1 -= 1
                p2 += 1

            return s[p1:p2+1]

        for i in range(len(s)-1):
            poly1 = expand(i, i)
            poly2 = expand(i, i+1)
            best = poly1 if len(poly1) > len(poly2) else poly2
            longest = best if len(best) > len(longest) else longest

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

    t1 = s.longestPalindrome("a")
    if t1 == "a":
        print("OK 4")

    t1 = s.longest_palindrome_expand("123456")
    if t1 == "1":
        print("OK 1")

    t1 = s.longest_palindrome_expand("babad")
    if t1 == "bab" or t1 == "aba":
        print("OK 2")

    t1 = s.longest_palindrome_expand("cbbd")
    if t1 == "bb":
        print("OK 3")

    t1 = s.longest_palindrome_expand("a")
    if t1 == "a":
        print("OK 4")
