class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # SORT
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            target = -nums[i]
            # TWO POINTERS
            while l < r:
                total = nums[l] + nums[r]
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # DEDUPE
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
                
        

        