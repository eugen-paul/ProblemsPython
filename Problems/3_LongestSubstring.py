class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos1 = 0
        max_value = 0
        unique_set = set()

        for c in s:
            if c in unique_set:
                while s[pos1] != c:
                    unique_set.remove(s[pos1])
                    pos1 += 1
                pos1 += 1
            else:
                unique_set.add(c)
                max_value = max(max_value, len(unique_set))
        return max_value


if __name__ == "__main__":
    s = Solution()
    if s.lengthOfLongestSubstring("abcabcbb") == 3:
        print("Ok 1")
    if s.lengthOfLongestSubstring("bbbbb") == 1:
        print("Ok 2")
    if s.lengthOfLongestSubstring("pwwkew") == 3:
        print("Ok 3")
