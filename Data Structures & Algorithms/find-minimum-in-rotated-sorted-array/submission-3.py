class Solution:
    def findMin(self, nums: List[int]) -> int:
        # INIT LR
        L, R = 0, len(nums) - 1
        while L < R:
            mid = (L + R) // 2
            # MID VS RIGHT
            if nums[mid] > nums[R]:
                # SHRINK
                L = mid + 1
            else:
                R = mid
        # RETURN L
        return nums[L]
        

        
        
