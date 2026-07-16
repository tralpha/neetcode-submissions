class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # SORT
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            # EXTEND OR APPEND
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        # RETURN MERGED
        return merged
        
        
        
        
        