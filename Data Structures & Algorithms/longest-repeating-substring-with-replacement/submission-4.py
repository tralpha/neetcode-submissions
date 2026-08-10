class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, max_freq, best = 0, 0, 0
        count = Counter()
        for R in range(len(s)):
            # WIN-COUNT
            count[s[R]] += 1
            # TRACK MAX
            max_freq = max(max_freq, count[s[R]])
            # SHRINK IF INVALID
            if (R - L + 1) - max_freq > k:
                count[s[L]] -= 1
                L += 1
            # UPDATE BEST
            best = max(best, (R - L + 1))
        return best
        