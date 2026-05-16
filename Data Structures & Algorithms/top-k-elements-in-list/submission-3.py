class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1
        
        buckets = [[] for _ in range(len(nums))]
        for n in counts:
            buckets[counts[n] - 1].append(n)
        
        results = []
        for i in range(len(nums), 0, -1):
            results.extend(buckets[i - 1])
        
        return results[:k]



