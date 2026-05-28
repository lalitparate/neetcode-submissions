class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowk  = defaultdict(set)
        columnk = defaultdict(set)

        squarek = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rowk[r] or board[r][c] in columnk[c] or board[r][c] in squarek[(r//3, c//3)]:
                    return False
                rowk[r].add(board[r][c])
                columnk[c].add(board[r][c])
                squarek[(r//3, c//3)].add(board[r][c])
        return True

        