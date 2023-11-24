class Solution {
    public int maxCoins(int[] piles) {
        Arrays.sort(piles);
        int z=(piles.length)/3;
        int ans=0;
        for(int i=piles.length-2;i>=piles.length-z*2;i-=2){
            ans+=piles[i];
        }
        return ans;
    }
}