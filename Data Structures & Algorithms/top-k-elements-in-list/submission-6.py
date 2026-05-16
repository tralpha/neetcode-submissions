class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
        buckets = [[] for _ in range(len(nums) + 1)]

        n = len(nums)
        output = []
        for num in freqs:
            buckets[freqs[num]].append(num)
        for i in range(n, -1, -1):
            for bucket_num in buckets[i]:
                output.append(bucket_num)
                if len(output) == k:
                    return output
        return output

