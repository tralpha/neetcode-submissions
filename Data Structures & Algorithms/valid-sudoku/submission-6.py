class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_r = defaultdict(set)
        seen_c = defaultdict(set)
        seen_sq = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen_r[r] or board[r][c] in seen_c[c] or board[r][c] in seen_sq[tuple([r//3, c//3])]:
                    return False
                
                seen_r[r].add(board[r][c])
                seen_c[c].add(board[r][c])
                seen_sq[tuple([r // 3, c // 3])].add(board[r][c])
        return True




            


        