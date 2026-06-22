class Solution:
    def findMin(self, nums: List[int]) -> int:
        # INIT L/R
        L, R = 0, len(nums) - 1
        while L < R:
            # MID VS RIGHT
            mid = (L + R) // 2
            if nums[mid] > nums[R]:
                # SHRINK
                L = mid + 1
            else:
                R = mid
        # Return left
        return nums[L]
        
