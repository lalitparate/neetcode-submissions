class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i, num in enumerate(nums):
           dct[num] = i


        for i, num in enumerate(nums):
            comp = target - num
            if comp in dct and i != dct[comp]:
                return [i, dct[comp]]
        return []