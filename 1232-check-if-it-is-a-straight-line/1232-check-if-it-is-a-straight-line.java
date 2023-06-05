class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
        double m1 = Double.POSITIVE_INFINITY;
        if(coordinates[1][0]-coordinates[0][0]!=0){
            m1=(coordinates[1][1]-coordinates[0][1])/(double)(coordinates[1][0]-coordinates[0][0]);
        }
        double m;
        for(int i=1;i<coordinates.length;i++){
            if(coordinates[i][0]-coordinates[i-1][0]==0){
                m=Double.POSITIVE_INFINITY;
            }
            else{
                m=(coordinates[i][1]-coordinates[i-1][1])/(double)(coordinates[i][0]-coordinates[i-1][0]);
            }
            if(m!=m1){
                
                return false;
            }
            
        }
        return true;
    }
}