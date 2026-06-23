class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # SORT BY START
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        # EXTEND OR APPEND
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        # RETURN MERGED
        return merged
