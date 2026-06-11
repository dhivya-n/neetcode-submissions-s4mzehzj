from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        events = []
        for interval in intervals:
            events.append([interval[0], +1])
            events.append([interval[1], -1])
        events.sort(key=lambda x: (x[0], -x[1]))

        start, end = -1, -1
        s = 0
        for event in events:
            if start == -1:
                start = event[0]
            s+=event[1]
            if s == 0:
                end = event[0]
                result.append([start, end])
                start, end = -1, -1
        return result
    
# Runtime
# 14
# ms
# Beats
# 7.79%
# Memory
# 25.28
# MB
# Beats
# 7.75%