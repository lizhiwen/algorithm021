class Solution:
    def isVaildSudoku(self,board) -> bool:
        def isVaildNine(lst):
            nums = list(filter(lambda x:x != '.', lst))
            return len(set(nums)) == len(nums)
        
        for row in board:
            if not isVaildNine(row):
                return False
        
        for column in zip(*board):
            if not isVaildNine(column):
                return False
        
        for row in range(3):
            for column in range(3):
                tmp = [board[i][j] for i in range(row*3,row*3+3) for j in range(column*3,column*3+3)]
                if not isVaildNine(tmp):
                    return False
        return True
    
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
print(Solution().isVaildSudoku(board))
