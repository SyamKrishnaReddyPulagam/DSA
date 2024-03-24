class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        grid=[[set() for _ in range(3)]for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    if board[i][j] in row[i]:
                        return False
                    row[i].add(board[i][j])
                    if board[i][j] in col[j]:
                        return False
                    col[j].add(board[i][j])
                    a,b=i//3,j//3
                    if board[i][j] in grid[a][b]:
                        return False
                    grid[a][b].add(board[i][j])
        return True