class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = defaultdict(int)

        for num in nums:
            my_dict[num] += 1
        
        my_list = list(my_dict.items())
        sorted_array = sorted(my_list, key=lambda x : x[1], reverse=True)
        
        return [x[0] for x in sorted_array][:k]