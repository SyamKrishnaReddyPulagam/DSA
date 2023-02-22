class Solution(object):
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c :
            return mat 
        y = 0
        arr = []
        x = []
        for i in range(m):
            for j in range(n):
                x.append(mat[i][j])
                y+=1
                if y == c:
                    arr.append(x)
                    x = []
                    y = 0
        return arr