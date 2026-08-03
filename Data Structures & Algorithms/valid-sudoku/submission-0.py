class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set) # hashmap
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": # if it's empty, continue
                    continue
                if (board[r][c] in rows[r] or # if weve seen the current value in the row, 
                    board[r][c] in cols[c] or # its a duplicate. same with col
                    board[r][c] in squares[(r // 3, c // 3)]): 
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

        return True