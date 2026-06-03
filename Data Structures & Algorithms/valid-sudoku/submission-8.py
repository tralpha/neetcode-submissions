class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                box = board[r][c]
                if box == ".":
                    continue
                sq_idx = (r // 3, c // 3)
                if box in rows[r] or box in cols[c] or box in squares[sq_idx]:
                    return False
                rows[r].add(box)
                cols[c].add(box)
                squares[sq_idx].add(box)
        return True