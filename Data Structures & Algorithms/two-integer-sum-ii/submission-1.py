class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            l = i + 1
            n = len(numbers)
            r = n-1
            tmp = target - numbers[i]
            while l<=r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1

        return []        
