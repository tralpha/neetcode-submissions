class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            s_tuple = tuple(sorted(tuple(s)))
            hmap[s_tuple].append(s)
        return list(hmap.values())

        

        