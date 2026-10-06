class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        for c in range(9):
            for r in range(9):
                val = board[r][c]
                if val == '.': continue
                if (val in cols[c] 
                or val in rows[r] 
                or val in squares[(r//3)*3+c//3]):
                    return False
                cols[c].add(val)
                rows[r].add(val)
                squares[(r//3)*3+c//3].add(board[r][c])
        return True
        
        