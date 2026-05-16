class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        res = nums[0]
        for num in nums:
            curSum = max(num, num + curSum)
            res = max(res, curSum)
        return res
        

        
        