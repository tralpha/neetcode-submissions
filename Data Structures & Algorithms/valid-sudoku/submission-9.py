class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(9):
            for c in range(9):
                box = board[r][c]
                if box == '.':
                    continue
                if box in rows[r] or box in cols[c] or box in squares[(r//3, c//3)]:
                    return False
                rows[r].add(box)
                cols[c].add(box)
                squares[(r//3, c//3)].add(box)
        return True
        