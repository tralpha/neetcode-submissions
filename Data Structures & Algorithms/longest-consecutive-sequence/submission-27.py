class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # SET
        numSet = set(nums)
        best = 0
        for num in numSet:
            # START
            if num - 1 not in numSet:
                length = 1
                # EXPAND
                while num + length in numSet:
                    length += 1
                best = max(best, length)
        return best
        