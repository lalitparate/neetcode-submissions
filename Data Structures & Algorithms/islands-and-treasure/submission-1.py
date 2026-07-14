class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = deque([(r, c)])
            visit = [[False]*COLS for _ in range(ROWS)]
            visit[r][c] = True
            steps = 0
            while q:
                n = len(q)
                for _ in range(n):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dr, dc in directions:
                        nr = row + dr
                        nc = col + dc
                        if (nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and not visit[nr][nc] and grid[nr][nc] != -1):
                            visit[nr][nc] = True
                            q.append((nr, nc))
                steps += 1
            return INF
                 


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)