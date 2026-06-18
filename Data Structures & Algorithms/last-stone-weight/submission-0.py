class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        
        heapq.heapify(stones)
        while(len(stones) > 1):
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))
            print(first, second)

            if second < first:
                heapq.heappush(stones, second - first)
        stones.append(0)
        return abs(stones[0])