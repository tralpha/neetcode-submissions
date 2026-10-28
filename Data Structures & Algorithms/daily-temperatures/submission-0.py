class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # INIT ZEROS
        res = [0,] * len(temperatures)
        # MONOTONICALLY DECREASING STACK
        stack = []
        # POP WHILE WARMER
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
                # APPEND
            stack.append(i)
        return res
                
        