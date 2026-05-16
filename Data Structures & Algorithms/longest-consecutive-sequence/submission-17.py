class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # start of a sequence: if num - 1 not in sequence
        # use a while loop to iterate please
        # us max(length, longest) to determine
        num_set = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in num_set:
                length = 1
                while (num + length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest
