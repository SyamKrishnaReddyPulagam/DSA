class Solution(object):
    def solveNQueens(self, n):
        def issafe(row,col,board,n):
            row1,col1=row,col
            
            #upper diagnol
            while row1>=0 and col1>=0:
                if board[row1][col1]=="Q":
                    return False
                row1-=1
                col1-=1
             
            #row
            row1,col1=row,col
            while col1>=0:
                if board[row1][col1]=="Q":
                    return False
                col1-=1
            
            #column
            col1=col
            while row1<n and col1>=0:
                if board[row1][col1]=="Q":
                    return False
                row1+=1
                col1-=1
            
            return True
        def func(col,board,n,ans):
            if col==n:
                temp=[]
                for i in board:
                    temp.append("".join(i))
                ans.append(temp)
                return
            for r in range(n):
                if issafe(r,col,board,n):
                    board[r][col]="Q"
                    func(col+1,board,n,ans)
                    board[r][col]="."
        ans=[]
        board=[["." for _ in range(n)]for _ in range(n)]
        func(0,board,n,ans)
        return ans
                