class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curr = nums[0], 0
        for num in nums:
            if curr < 0:
                curr = 0
            curr += num
            maxSub = max(curr, maxSub)
        return maxSub

        
        