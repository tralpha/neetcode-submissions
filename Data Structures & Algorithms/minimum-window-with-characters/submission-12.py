class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # NEED MAP
        have, need = Counter(), Counter(t)
        have_unique, need_unique = 0, len(need)
        l, best_l, best_len = 0, 0, float("inf")
        # EXPAND R
        for r in range(len(s)):
            have[s[r]] += 1
            # MATCH CHECK
            if s[r] in need and have[s[r]] == need[s[r]]:
                have_unique += 1
            # SHRINK UNTIL VALID
            while have_unique == need_unique:
                new_len = r - l + 1
                if new_len < best_len:
                    best_len = new_len
                    best_l = l
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    have_unique -= 1
                l += 1
        return s[best_l:best_l + best_len] if best_len < float("inf") else ""