class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        maxIslands = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            res = 1
            while(q):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    res += 1
            return res


        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    val = bfs(r, c)
                    maxIslands = max(val, maxIslands)
        return maxIslands