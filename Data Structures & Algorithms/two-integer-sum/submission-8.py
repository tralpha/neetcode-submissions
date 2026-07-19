class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # diff -> idx
        # SCAN
        for i, num in enumerate(nums):
            # LOOKUP
            if num in seen:
                return [seen[num], i]
            diff = target - num
            seen[diff] = i
        