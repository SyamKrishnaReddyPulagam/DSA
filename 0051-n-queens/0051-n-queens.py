class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        posD,negD=set(),set()
        ans=[]
        board=[["."]*n for i in range(n)]
        def func(r):
            if r==n:
                temp=["".join(i) for i in board]
                ans.append(temp)
                return
            for c in range(n):
                if c in col or (r+c) in posD or (r-c) in negD:
                    continue
                col.add(c)
                posD.add(r+c)
                negD.add(r-c)
                board[r][c]="Q"
                
                func(r+1)
                
                col.remove(c)
                posD.remove(r+c)
                negD.remove(r-c)
                board[r][c]="."
        func(0)
        return ans