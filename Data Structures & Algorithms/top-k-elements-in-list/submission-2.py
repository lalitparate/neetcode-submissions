class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = defaultdict(int)
        for num in nums:
            my_dict[num] += 1

        heap = []

        for num in my_dict.keys():
            heapq.heappush(heap, (my_dict[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res



        
        
