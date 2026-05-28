class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = defaultdict(int)
        my_list = []
        for i in range(-1000, 1001, 1):
            my_list.append([i, 0])
        for num in nums:
            my_list[num+1000][1] += 1
        print(my_list[1003])

        sorted_arr = sorted(my_list, key=lambda x: x[1], reverse=True)
        return [x[0] for x in sorted_arr][:k]

        
        
