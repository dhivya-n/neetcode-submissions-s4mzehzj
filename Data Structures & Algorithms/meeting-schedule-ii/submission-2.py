
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #sort the intervals
        intervals.sort(key=lambda x:x.start)
        if len(intervals) == 0:
            return 0
        heap = []
        heapq.heappush(heap, intervals[0].end)
        for i in range(1, len(intervals)):
            if intervals[i].start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
        return len(heap)