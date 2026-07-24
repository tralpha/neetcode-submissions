class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # LENGTH
        if len(s) != len(t):
            return False
        # COUNT
        counts = [0,] * 26
        # COMPARE
        for c1, c2 in zip(s, t):
            counts[ord(c1) - ord('a')] += 1
            counts[ord(c2) - ord('a')] -= 1
        return all(count == 0 for count in counts)
        


        

        