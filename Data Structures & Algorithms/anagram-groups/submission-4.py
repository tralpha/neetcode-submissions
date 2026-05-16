class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            s_list = [0,] * 26
            for c in s:
                s_list[ord(c) - ord('a')] += 1
            hmap[tuple(s_list)].append(s)
        return list(hmap.values())

        

        