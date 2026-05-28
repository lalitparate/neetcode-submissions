class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        
        A.sort()
        i = 0
        j = len(nums) - 1

        while (i<j):
            sm = A[i][0] + A[j][0]
            if sm == target:
                if A[i][1] < A[j][1]:
                    return [A[i][1], A[j][1]]
                else:
                    return [A[j][1], A[i][1]]
            elif sm < target:
                i += 1
            else:
                j -= 1


            
