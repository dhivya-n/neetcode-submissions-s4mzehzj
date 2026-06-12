class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = defaultdict(int)
        for interval in intervals:
            events[interval.start] += 1
            events[interval.end] -= 1
        prefix_sum = 0
        max_rooms = 0
        for index in sorted(events):
            prefix_sum+=events[index]
            if prefix_sum > max_rooms:
                max_rooms = prefix_sum
        return max_rooms