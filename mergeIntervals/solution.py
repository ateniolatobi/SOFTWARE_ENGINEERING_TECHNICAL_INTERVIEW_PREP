class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x[0])
        start, end = intervals[0][0], intervals[0][1]
        out = []
        for interval in intervals:
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                out.append([start, end])
                start, end = interval[0], interval[1]
                
        out.append([start, end])
        return out
