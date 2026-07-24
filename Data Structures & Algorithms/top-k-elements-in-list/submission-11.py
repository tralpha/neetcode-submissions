class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        # COUNT
        counts = Counter(nums)
        # BUCKETS
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            buckets[count].append(num)
        # SWEEP
        for bucket in range(len(nums), 0, -1):
            for n in buckets[bucket]:
                res.append(n)
                if len(res) == k:
                    return res
        return []
        