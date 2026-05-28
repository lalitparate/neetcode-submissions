class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in dct:
                return [dct[comp], i]
            dct[num] = i