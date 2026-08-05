class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # INIT LR
        L, R = 0, len(heights) - 1
        best = 0
        while L < R:
            # AREA
            area = (R - L) * min(heights[L], heights[R])
            # UPDATE
            best = max(area, best)
            # MOVE
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return best
        
