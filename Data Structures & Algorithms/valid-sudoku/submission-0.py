class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            s = set()
            for j in i:
                if j == ".":
                    continue
                if j in s:
                    return False
                else:
                    s.add(j)

        for i in range(0,len(board[0])):
            s = set()
            for j in range(0,len(board)):
                if board[j][i] == ".":
                    continue
                if board[j][i] in s:
                    return False
                else:
                    s.add(board[j][i])

        
        for square in range(9):
            s = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in s:
                        return False
                    s.add(board[row][col])
                    
        return True