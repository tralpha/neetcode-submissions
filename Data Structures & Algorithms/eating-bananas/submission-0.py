class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # BINARY SEARCH ON ANSWER
        L, R = 1, max(piles)
        while L <= R:
            k = (L + R) // 2
            # SIM HOURS
            hours = sum((p + k - 1) // k for p in piles)
            # SHRINK IF FEASIBLE
            if hours <= h:
                R = k - 1
            else:
                L = k + 1
        # RETURN L
        return L
        