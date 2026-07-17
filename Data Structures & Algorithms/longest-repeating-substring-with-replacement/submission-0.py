class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, best, max_freq = 0, 0, 0
        count = Counter()
        # EXPAND R
        for R in range(len(s)):
            count[s[R]] += 1
            # TRACK MAX
            max_freq = max(count[s[R]], max_freq)
            win_size = R - L + 1
            # SHRINK WHILE INVALID
            if win_size - max_freq > k:
                count[s[L]] -= 1
                L += 1
            # TRACK_BEST
            best = max(best, R - L + 1)
        return best
        