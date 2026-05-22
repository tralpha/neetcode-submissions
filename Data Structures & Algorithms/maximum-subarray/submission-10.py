class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum, maxSum = 0, nums[0]
        for num in nums:
            curSum = max(num, curSum + num)
            maxSum = max(curSum, maxSum)
        return maxSum

        

        
        