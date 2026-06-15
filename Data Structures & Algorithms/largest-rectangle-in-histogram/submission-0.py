class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # MON-INC-STACK
        stack = []
        best = 0

        # SENTINEL FLUSH
        for i, h in enumerate(heights + [0]):
            while stack and h < heights[stack[-1]]:
                top = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                area = heights[top] * width
                best = max(best, area)
            stack.append(i)
        return best
