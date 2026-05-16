class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return sum(nums)
        
        largest_sums = defaultdict(int) # i,j --> sum; i = idx to start, j = num of int to sum after this
        for i, num in enumerate(nums):
            # largest_sums[tuple([i,0])]
            for j in range(i + 1, len(nums) + 1):
                n_to_sum = nums[i:j]
                largest_sums[tuple([i,j])] = sum(n_to_sum)
        return max(list(largest_sums.values()))


                # # if i == j:
                # #     largest_sums(tuple([i,j])) = 
                # if j > i:
                #     for k in range(j, nums):

        

        
        