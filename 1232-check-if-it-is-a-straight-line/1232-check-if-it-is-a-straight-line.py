class Solution(object):
    def checkStraightLine(self, coordinates):
        if (coordinates[1][0]-coordinates[0][0])==0:
            slope=float('inf')
        else:
            slope =(coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        m1=0
        for i in range(2,len(coordinates)):
            if (coordinates[i][0]-coordinates[i-1][0])==0:
                m1=float('inf')
            else:
                m1=(coordinates[i][1]-coordinates[i-1][1])/(coordinates[i][0]-coordinates[i-1][0])
            if m1!=slope:
                       return False
        return True