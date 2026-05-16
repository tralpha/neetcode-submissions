class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # for each num, find out the 
        largest = max(nums)
        curr = 0
        for i in range(len(nums)):
            curr = curr + nums[i]
            if curr < 0:
                curr = 0
                continue
            largest = max(curr, largest)
        return largest
            


        
        