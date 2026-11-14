class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        # COUNT
        for s in strs:
            counts = [0,] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            # TUPLE AS KEY
            groups[tuple(counts)].append(s)
        # GROUP
        return list(groups.values())
        