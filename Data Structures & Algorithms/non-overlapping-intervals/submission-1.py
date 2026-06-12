
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        result = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                intervals[i][1] = min(intervals[i-1][1], intervals[i][1])
                result+=1
        return result
