class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # SORT
        nums.sort()
        res = []
        for i in range(len(nums)):
            # DEDUPE
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            # TWO SUM
            L, R = i + 1, len(nums) - 1
            while L < R:
                total = nums[L] + nums[R]
                if total < target:
                    L += 1
                elif total > target:
                    R -= 1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
        return res
