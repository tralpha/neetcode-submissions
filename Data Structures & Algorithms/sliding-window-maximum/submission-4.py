class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = r = 0
        output = []

        while r < len(nums):
            # empty the q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            

            # check whether l is more than q[0]
            if l > q[0]:
                q.popleft()

            # check if r+1 >= q, and update output
            if (r+1) >= k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output

        