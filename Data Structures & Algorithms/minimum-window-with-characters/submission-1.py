class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        have = {}
        need = {}
        have_unique, need_unique = 0, 0
        l, r = 0, 0
        res, res_len = [-1, -1], float('inf')
        for c in t:
            need[c] = 1 + need.get(c, 0)
        need_unique = len(need)
        for r in range(len(s)):
            # expand
            c = s[r]
            have[c] = 1 + have.get(c, 0)
            if c in need and have[c] == need[c]:
                have_unique += 1
            
            # while shrink
            while have_unique == need_unique:
                if (r - l + 1) < res_len:
                    res, res_len = [l, r], r - l + 1
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    have_unique -= 1
                l+=1
        return s[res[0]:res[1]+1] if res_len != float('inf') else ""
                


            
            
        