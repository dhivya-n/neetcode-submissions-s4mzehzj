class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        toRemove = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                if intervals[i-1][1] < intervals[i][1]:
                    intervals[i][1] = intervals[i-1][1]
                    intervals[i][0] = intervals[i-1][0]
                toRemove+=1
        return toRemove