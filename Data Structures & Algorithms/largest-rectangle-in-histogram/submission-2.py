class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best = 0
        # SENTINEL FLASH
        for i, h in enumerate(heights + [0]):
            # POP WHILE SHORTER
            while stack and h < heights[stack[-1]]:
                top = stack.pop()
                # AREA FROM WIDTH
                width = i if not stack else i - stack[-1] - 1
                area = heights[top] * width
                best = max(best, area)
            # APPEND
            stack.append(i)
        return best