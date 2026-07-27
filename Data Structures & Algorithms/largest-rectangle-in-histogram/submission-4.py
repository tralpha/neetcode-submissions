class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best = 0
        # MONOTONICALLY INCREASING
        stack = []
        # SENTINEL FLUSH
        for i, h in enumerate(heights + [0]):
            # POP WHILE SHORTER
            while stack and h < heights[stack[-1]]:
                top = stack.pop()
                # AREA FROM WIDTH
                width = i if not stack else i - stack[-1] - 1
                area = heights[top] * width
                best = max(area, best)
            # APPEND
            stack.append(i)
        return best        