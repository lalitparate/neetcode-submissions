class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hshSet = set()
        for num in nums:
            if num in hshSet:
                return num
            hshSet.add(num)
            