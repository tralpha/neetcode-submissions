class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == ".":
                    continue
                sq_idx = (r//3, c//3)
                if cell in rows[r] or cell in cols[c] or cell in squares[sq_idx]:
                    return False
                rows[r].add(cell)
                cols[c].add(cell)
                squares[sq_idx].add(cell)
        return True
        