class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = defaultdict(int)
        count_s = [0]*26
        count_t = [0]*26
        for c in s:
            count_s[ord(c)-ord('a')] += 1
        for c in t:
            count_t[ord(c)-ord('a')] += 1
        return tuple(count_s) == tuple(count_t)
        

        