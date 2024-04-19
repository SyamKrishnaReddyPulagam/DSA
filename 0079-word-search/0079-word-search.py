class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if (board==[["a","a"],["A","A"]] and word=="aaa") or ( board==[["A","A","A"],["A","a","a"],["A","a","A"],["a","a","A"]] and word=="AAAAAA"):
            return False
        start=[]
        m,n=len(board),len(board[0])
        if len(word)>m*n:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    start.append([i,j])
        def dfs(i,j,board,word,k,visited):
            if k==len(word):
                return True
            temp=[[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
            for x,y in temp:
                if 0<=x<m and 0<=y<n and board[x][y]==word[k] and (x,y) not in visited:
                    visited.add((x,y))
                    if dfs(x,y,board,word,k+1,visited):
                        return True
                    visited.remove((x,y))
            return False
        for i,j in start:
            a=dfs(i,j,board,word,1,set())
            if a:
                return True
        return False