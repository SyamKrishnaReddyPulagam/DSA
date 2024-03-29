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
    int bottomup(vector<int> v){
        int n=v.size();
        vector<vector<int>> dp(n,vector<int>(n,0));
        for(int i=n-1;i>=0;i--){
            for(int j=i+2;j<n;j++){
                int a=INT_MAX;
                for(int k=i+1;k<j;k++){
                    a=min(a,v[i]*v[j]*v[k]+dp[i][k]+dp[k][j]);
                }
                dp[i][j]=a;
            }
        }
        return dp[0][n-1];
    }
    int minScoreTriangulation(vector<int>& values) {
        int n=values.size();
        vector<vector<int>> dp(n,vector<int>(n,-1));
        return topdown(values,0,n-1,dp);
        //return bottomup(values);
    }
};