class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.meanHeap = nums
        self.k = k
        heapq.heapify(self.meanHeap)
        while(len(self.meanHeap)> k):
            heapq.heappop(self.meanHeap)


    def add(self, val: int) -> int:
        heapq.heappush(self.meanHeap, val)
        if len(self.meanHeap) > self.k:
            heapq.heappop(self.meanHeap)
        return self.meanHeap[0]
        
