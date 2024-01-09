class Solution:
    def totalNQueens(self, n: int) -> int:
        col,posD,negD=set(),set(),set()
        ans=0
        board=[["."]*n for i in range(n)]
        def func(row):
            if row==n:
                nonlocal ans
                ans+=1
                return
            for c in range(n):
                if c in col or (row+c) in posD or (row-c) in negD:
                    continue
                col.add(c)
                posD.add(row+c)
                negD.add(row-c)
                
                func(row+1)
                
                col.remove(c)
                posD.remove(row+c)
                negD.remove(row-c)
        func(0)
        return ans
                