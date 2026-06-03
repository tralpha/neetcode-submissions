class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        # COUNT
        for s in strs:
            counts = [0,] * 26
            for c in s:
                pos = ord(c) - ord('a')
                counts[pos] += 1
            # TUPLE AS KEY
            anagrams[tuple(counts)].append(s)
        return list(anagrams.values())
        
