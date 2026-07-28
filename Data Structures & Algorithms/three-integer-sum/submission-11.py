class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # SORT
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # FIX
            target = -nums[i]
            # TWO POINTERS
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
                    # DEDUPE
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
        return res
        