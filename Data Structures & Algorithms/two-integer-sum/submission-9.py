class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        # SCAN
        for idx, num in enumerate(nums):
            # LOOKUP
            if num in seen:
                # RETURN
                return [seen[num], idx]
            diff = target - num
            # STORE
            seen[diff] = idx
        