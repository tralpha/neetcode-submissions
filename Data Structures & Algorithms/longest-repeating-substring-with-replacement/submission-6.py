class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, max_freq, best = 0, 0, 0
        count = Counter()
        # EXPAND R
        for R in range(len(s)):
            count[s[R]] += 1
            # TRACK MAX
            max_freq = max(count[s[R]], max_freq)
            # SHRING WHILE INVALID
            if (R - L + 1) - max_freq > k:
                count[s[L]] -= 1
                L += 1
            best = max(R - L + 1, best)
        return best

