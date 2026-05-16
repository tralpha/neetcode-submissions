class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # NEED MAP
        need = Counter(t)
        need_unique = len(need)
        have = Counter()
        have_unique = 0
        L = 0
        best_len = float("inf")
        best_l = 0

        # EXPAND R
        for R in range(len(s)):
            c = s[R]
            have[c] += 1
            # MATCH - CHECK
            if c in need and have[c] == need[c]:
                have_unique += 1
            # SHRINK WHILE VALID
            while need_unique == have_unique:
                new_len = R - L + 1
                if new_len < best_len:
                    best_len = new_len
                    best_l = L
                c = s[L]
                have[c] -= 1
                if c in need and have[c] < need[c]:
                    have_unique -= 1
                L += 1
        return s[best_l:best_l + best_len] if best_len < float("inf") else ""