import heapq

class MedianFinder:
    def __init__(self):
        self.minheap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        if(len(self.maxHeap) == 0):
            heapq.heappush(self.maxHeap, -num)
            return 
        
        if num > -self.maxHeap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxHeap, -num)   

        #rebalance
        min_l = len(self.minheap)
        max_l = len(self.maxHeap)
        if max_l-min_l >= 2:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxHeap)) 
        elif min_l-max_l >=2:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minheap)) 


    def findMedian(self) -> float:
        n = len(self.maxHeap) + len(self.minheap)
        if n%2 == 0:
            return (-self.maxHeap[0] + self.minheap[0]) / 2
        else:
             return -self.maxHeap[0] if len(self.maxHeap) > len(self.minheap) else self.minheap[0]
        