class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        L, R = 0, len(height) - 1
        max_l, max_r = height[L], height[R]
        water = 0
        while L < R:
            # SMALLER MAX
            if max_l < max_r:
                # MOVE
                L += 1
                # UPDATE
                max_l = max(max_l, height[L])
                # CALC
                water += max_l - height[L]
            else:
                R -= 1
                max_r = max(max_r, height[R])
                water += max_r - height[R]
        return water