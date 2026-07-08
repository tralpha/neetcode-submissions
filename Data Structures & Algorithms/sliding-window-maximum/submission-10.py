class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # decreasing
        l = 0
        res = []
        for r in range(len(nums)):
            # pop back
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            # pop front
            if l > q[0]:
                q.popleft()
            # append
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
        return res


        

            


        