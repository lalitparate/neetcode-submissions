class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        mp = defaultdict(int)

        for i in range(n):
            tmp = target - numbers[i]
            if mp[tmp]:
                return [mp[tmp], i+1]

            mp[numbers[i]] = i + 1
        return []

 