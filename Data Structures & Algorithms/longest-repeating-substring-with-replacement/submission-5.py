class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, max_freq = 0, 0
        count = Counter()
        best = 0
        # EXPAND R
        for R in range(len(s)):
            count[s[R]] += 1
            # TRACK MAX
            max_freq = max(max_freq, count[s[R]])
            # SHRING IF INVALID
            if (R - L + 1) - max_freq > k:
                count[s[L]] -= 1
                L += 1
            best = max(R - L + 1, best)
        return best
            