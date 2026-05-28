class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        n = len(numbers)
        j = n-1

        while(i<j):
            print(i, j)
            tg = numbers[i] + numbers[j]
            if tg < target:
                i += 1
            elif tg > target:
                j -= 1
            else:
                return [i+1, j+1]
        
