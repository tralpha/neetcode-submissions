class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, best, max_freq = 0, 0, 0
        count = Counter()
        for R in range(len(s)):
            count[s[R]] += 1
            max_freq = max(count[s[R]], max_freq)
            win_size = R - L + 1
            if win_size - max_freq > k:
                count[s[L]] -= 1
                L += 1
            best = max(best, R - L + 1)
        return best