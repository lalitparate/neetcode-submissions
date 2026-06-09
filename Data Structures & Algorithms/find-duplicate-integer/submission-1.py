class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        old = None
        for num in nums:
            if num == old:
                return num
            old = num
