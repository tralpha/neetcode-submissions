class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = Counter()
        have_unique, need_unique = 0, len(need)
        best_l, best_len = 0, float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            have[c] += 1
            if c in need and have[c] == need[c]:
                have_unique += 1
            while have_unique == need_unique:
                new_len = r - l + 1
                if new_len < best_len:
                    best_len = new_len
                    best_l = l
                c = s[l]
                have[c] -= 1
                if c in need and have[c] < need[c]:
                    have_unique -= 1
                l += 1
        return s[best_l: best_l + best_len] if best_len != float('inf') else ""