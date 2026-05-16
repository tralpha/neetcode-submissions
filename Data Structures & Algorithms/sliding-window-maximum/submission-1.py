class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        j = 0
        res = []
        windows = len(nums) - k + 1
        for i in range(windows):
            curMax = max(nums[i:i + k])
            res.append(curMax)
        return res

        # mp = {}
        # l = 0
        # res = 0
        # for r in range(len(nums)):
        #     if s[r] in mp:
        #         l = max(mp[s[r]] + 1, l)
        #     mp[s[r]] = r
        #     res = max(res, r - l + 1)

        