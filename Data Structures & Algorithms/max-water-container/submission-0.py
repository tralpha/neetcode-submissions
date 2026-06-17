class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # INIT l, r
        l, r = 0, len(heights) - 1
        best = 0
        while l < r:
            # AREA
            area = min(heights[l], heights[r]) * (r - l)
            # UPDATE
            best = max(best, area)
            # MOVE
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return best
        