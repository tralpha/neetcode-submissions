class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counts = Counter(nums)
        buckets = [[] for _ in range(n + 1)]
        res = []
        for num, count in counts.items():
            buckets[count].append(num)
        for bucket in range(n, 0, -1):
            for num in buckets[bucket]:
                res.append(num)
                if len(res) == k:
                    return res
        return res


        
        