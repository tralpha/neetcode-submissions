class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq, best = 0, 0
        L = 0
        count = Counter()
        # EXPAND R
        for R in range(len(s)):
            count[s[R]] += 1
            # TRACK MAX
            max_freq = max(max_freq, count[s[R]])
            win_size = R - L + 1
            # SHRINK WHILE INVALID
            if win_size - max_freq > k:
                count[s[L]] -= 1
                L += 1
            # TRACK BEST
            best = max(best, R - L + 1)
        return best
        