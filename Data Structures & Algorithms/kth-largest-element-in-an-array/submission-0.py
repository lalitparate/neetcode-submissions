class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for val in nums:
            heapq.heappush(minHeap, val)
            k -= 1
            if k < 0:
                heapq.heappop(minHeap)
        
        return minHeap[0]
            
