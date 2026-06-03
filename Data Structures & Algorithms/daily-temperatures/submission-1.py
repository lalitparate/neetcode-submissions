class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonic decreasing stack 
        res = [0]*len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                tmp, ind = stack.pop()
                res[ind] = i - ind
            stack.append((temp, i))
        return res