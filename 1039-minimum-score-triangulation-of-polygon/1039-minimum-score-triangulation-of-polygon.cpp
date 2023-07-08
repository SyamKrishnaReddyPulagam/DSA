class Solution {
public:
    int topdown(vector<int> &v,int i,int j,vector<vector<int>> &dp){
        if(i+1==j){
            return 0;
        }
        if(dp[i][j]!=-1){
            return dp[i][j];
        }
        int a=INT_MAX;
        for(int k=i+1;k<j;k++){
            a=min(a,v[i]*v[j]*v[k]+topdown(v,i,k,dp)+topdown(v,k,j,dp));
        }
        dp[i][j]=a;
        return dp[i][j];
    }
    int minScoreTriangulation(vector<int>& values) {
        int n=values.size();
        vector<vector<int>> dp(n,vector<int>(n,-1));
        return topdown(values,0,n-1,dp);
    }
};