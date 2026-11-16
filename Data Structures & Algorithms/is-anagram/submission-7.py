class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = [0,] * 26
        for c1, c2 in zip(s, t):
            counts[ord(c1) - ord('a')] += 1
            counts[ord(c2) - ord('a')] -= 1
        return all([c == 0 for c in counts])
        