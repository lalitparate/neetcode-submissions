class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        fresh = 0
                
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        def addCell(r, c):
            nonlocal fresh
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return
            if grid[r][c] == 1:
                grid[r][c] = 2
                q.append((r,c))
                fresh -= 1
        
        minute = 0
        while fresh > 0 and q:
            n = len(q)
            print(q)
            for _ in range(n):
                rw, cl = q.popleft()
                addCell(rw+1, cl)
                addCell(rw-1, cl)
                addCell(rw, cl+1)
                addCell(rw, cl-1)
            minute += 1
        return minute if fresh == 0 else -1       