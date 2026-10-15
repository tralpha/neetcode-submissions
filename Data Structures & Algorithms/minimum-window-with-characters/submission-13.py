class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # NEED MAP
        need = Counter(t)
        have = Counter()
        need_unique = len(need)
        have_unique = 0
        best_l, L = 0, 0
        best_len = float('inf')
        # EXPAND R
        for R in range(len(s)):
            have[s[R]] += 1
            # MATCH CHECK
            if s[R] in need and have[s[R]] == need[s[R]]:
                have_unique += 1
            # SHRING WHILE VALID
            while have_unique == need_unique:
                window_len = R - L + 1
                if window_len < best_len:
                    best_len = window_len
                    best_l = L
                have[s[L]] -= 1
                if s[L] in need and have[s[L]] < need[s[L]]:
                    have_unique -= 1
                L += 1
        return s[best_l:best_l + best_len] if best_len != float('inf') else ""
        
        