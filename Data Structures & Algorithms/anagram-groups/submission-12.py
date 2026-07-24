class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)
        for s in strs:
            s_count = [0,] * 26
            for c in s:
                s_count[ord(c) - ord('a')] += 1
            counts[tuple(s_count)].append(s)
        return list(counts.values())
        