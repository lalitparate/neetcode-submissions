class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = 0
        maxR = 0
        res = 0
        if len(height) <= 1:
            return 0
        for i in range(len(height)):
            maxL = maxR = height[i]
            for j in range(i+1):
                maxL = max(maxL, height[j])
            
            for j in range(i+1, len(height)):
                maxR = max(maxR, height[j])
            
            res = res + min(maxR, maxL) - height[i]
        return res
