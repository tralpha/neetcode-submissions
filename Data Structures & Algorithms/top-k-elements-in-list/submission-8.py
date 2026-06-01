class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # COUNT
        freqs = Counter(nums)

        # BUCKET
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freqs.items():
            buckets[freq].append(num)

        # SWEEP
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for b in buckets[i]:
                res.append(b)
                if len(res) == k:
                    return res
