class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = [0,] * 26
        for c in s:
            n = ord(c) - ord('a')
            counts[n] += 1
        for c in t:
            n = ord(c) - ord('a')
            counts[n] -= 1
        return all(count == 0 for count in counts)


        

        