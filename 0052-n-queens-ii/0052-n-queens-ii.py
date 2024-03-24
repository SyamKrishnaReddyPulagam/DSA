class Solution(object):
    def totalNQueens(self, n):
        ans=[0]
        board=[["." for _ in range(n)] for _ in range(n)]
        def issafe(row,col,board,n):
            r,c=row,col
            #left upper diagnol
            while r>=0 and c>=0:
                if board[r][c]=="Q":
                    return False
                r-=1
                c-=1
            
            r,c=row,col
            #right lower diagnol
            while r<n and c>=0:
                if board[r][c]=="Q":
                    return False
                r+=1
                c-=1
            
            r,c=row,col
            #row 
            while c>=0:
                if board[r][c]=="Q":
                    return False
                c-=1
            return True
        def func(col,board,n,ans):
            if col==n:
                ans[0]+=1
                return
            for r in range(n):
                if issafe(r,col,board,n):
                    board[r][col]="Q"
                    func(col+1,board,n,ans)
                    board[r][col]="."
        func(0,board,n,ans)
        return ans[0]