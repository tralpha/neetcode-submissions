class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # DECREASE
        q = deque()
        l = 0
        res = []
        for r in range(len(nums)):
            # POP BACK
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            # POP FRONT
            if l > q[0]:
                q.popleft()
            # APPEND
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
        return res

            
        