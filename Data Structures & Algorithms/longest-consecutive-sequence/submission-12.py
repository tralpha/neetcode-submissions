class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int) # mapping of the number to the length of the longest consecutive integer
        res = 0

        for num in nums:
            if not mp[num]: # process only new numbers not yet seen
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res