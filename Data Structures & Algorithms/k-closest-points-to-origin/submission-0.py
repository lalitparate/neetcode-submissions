class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        
        for point in points:
            val = math.sqrt((0 - point[0])**2 + (0-point[1])**2)
            heap.append([val, point[0], point[1]])
        
        heapq.heapify(heap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(heap)
            res.append([x,y])
            k -= 1
        return res
