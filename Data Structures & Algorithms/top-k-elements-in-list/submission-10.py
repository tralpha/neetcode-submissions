class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        # COUNT
        freqs = Counter(nums)
        # BUCKET
        buckets = [[] for _ in range(n + 1)]
        for num, freq in freqs.items():
            buckets[freq].append(num)
        # SWEEP
        for bucket in range(n, 0, -1):
            for num in buckets[bucket]:
                res.append(num)
                if len(res) == k:
                    return res
        return res

        