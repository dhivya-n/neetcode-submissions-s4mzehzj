class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        if n == 0:
            return [newInterval]
        while i < n and intervals[i][0] < newInterval[0] and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i+=1
        if i == n:
            result.append(newInterval)
            return result
        start = min(intervals[i][0], newInterval[0])
        found = False
        while i < n and not found:
            if intervals[i][0] > newInterval[1]:
                result.append([start, newInterval[1]])
                found = True
            elif intervals[i][1] > newInterval[1]:
                result.append([start, intervals[i][1]])
                i+=1
                found = True
            else:
                i+=1
        if not found:
            result.append([start, newInterval[1]])     
        while i < n:
            result.append(intervals[i])
            i+=1
        return result

        

           
        