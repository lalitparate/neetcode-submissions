class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        maxIsland = 0
        visit = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or grid[r][c]==0:
                return 0
            visit.add((r,c))
            return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))          
                
        for r in range(ROWS):
            for c in range(COLS):
                val = dfs(r, c)
                maxIsland = max(val, maxIsland) 
        return maxIsland

