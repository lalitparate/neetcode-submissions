class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0

        if len(heights) <=1:
            return 0
        
        l = 0
        r = len(heights) - 1

        while(l < r):
            minHt = min(heights[l], heights[r])
            width = r-l
            nwS = minHt*width
            maxA = max(maxA, nwS)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        
        return maxA


        