class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, best = 0, 0
        charSet = set()
        for R in range(len(s)):
            while s[R] in charSet:
                charSet.remove(s[L])
                L += 1
            charSet.add(s[R])
            best = max(best, R - L + 1)
        return best