class neighborSum(object):

    def __init__(self, grid):
        self.grid=grid
        self.dicti={}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.dicti[grid[i][j]]=[i,j]
        
    def adjacentSum(self, value):
        top,down,left,right=0,0,0,0
        i,j=self.dicti[value]
        if i!=0:
            top=self.grid[i-1][j]
        if i!=len(self.grid)-1:
            down=self.grid[i+1][j]
        if j!=0:
            left=self.grid[i][j-1]
        if j!=len(self.grid[0])-1:
            right=self.grid[i][j+1]
        return top+down+left+right
        

    def diagonalSum(self, value):
        i,j=self.dicti[value]
        m,n=len(self.grid),len(self.grid[0])
        ans=0
        left_top,left_bottom,right_top,right_bottom=[i-1,j-1],[i+1,j-1],[i-1,j+1],[i+1,j+1]
        if left_top[0]>=0 and left_top[1]>=0 and left_top[0]<m and left_top[1]<n:
            ans+=self.grid[left_top[0]][left_top[1]]
        if left_bottom[0]>=0 and left_bottom[1]>=0 and left_bottom[0]<m and left_bottom[1]<n:
            ans+=self.grid[left_bottom[0]][left_bottom[1]]
        if right_top[0]>=0 and right_top[1]>=0 and right_top[0]<m and right_top[1]<n:
            ans+=self.grid[right_top[0]][right_top[1]]
        if right_bottom[0]>=0 and right_bottom[1]>=0 and right_bottom[0]<m and right_bottom[1]<n:
            ans+=self.grid[right_bottom[0]][right_bottom[1]]
        return ans
        
        
        


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)