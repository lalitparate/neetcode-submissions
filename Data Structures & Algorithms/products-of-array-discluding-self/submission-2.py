class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero_count = 0
        prod = 1
        for num in nums:
            if num:
                prod *= num
            else:
                zero_count += 1
        
        if zero_count > 1: return [0]*n

        res = [0]*n

        for i, c in enumerate(nums):
            if zero_count:
                if c:
                    res[i] = 0
                else:
                    res[i] = prod
            else:
                res[i] = prod//c
        return res

       