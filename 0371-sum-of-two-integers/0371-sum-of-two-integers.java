class Solution {
    public int getSum(int a, int b) {
        while(b!=0){
            int z=(a&b)<<1;
            a=a^b;
            b=z;
        }
        return a;
    }
}