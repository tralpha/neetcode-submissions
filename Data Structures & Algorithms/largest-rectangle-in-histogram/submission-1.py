class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best = 0
        # SENTINEL FLUSH
        for i, h in enumerate(heights + [0]):
            # POP WHILE SHORTER
            while stack and h < heights[stack[-1]]:
                top = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                # AREA FROM WIDTH
                area = width * heights[top]
                best = max(best, area)
            # APPEND
            stack.append(i)
        return best
        

        
