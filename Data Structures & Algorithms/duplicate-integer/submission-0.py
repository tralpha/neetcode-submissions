class Solution:
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     freq = {} # num -> freqq
    #     for num in nums:
    #         if num in freq.keys():
    #             return True
    #         else:
    #             freq[num] = 1 + freq.get(num, 0)
    #     return False

    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for n in nums:
            if n in seen:
                return True
            else:
                seen.append(n)
        return False

        