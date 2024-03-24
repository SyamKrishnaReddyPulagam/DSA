class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def issafe(num,row,col,board):
            for i in range(0,9):
                if board[i][col]==num:
                    return False
                if board[row][i]==num:
                    return False
            a,b=row//3,col//3
            dicti={0:0,1:3,2:6}
            for i in range(dicti[a],dicti[a]+3,1):
                for j in range(dicti[b],dicti[b]+3,1):
                    if board[i][j]==num:
                        return False
            return True
        def func(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]==".":
                        for k in range(1,10):
                            if issafe(str(k),i,j,board):
                                board[i][j]=str(k)
                                if(func(board)==True):
                                    return True
                                else:
                                    board[i][j]="."
                        return False
            return True
        func(board)
                                
                                