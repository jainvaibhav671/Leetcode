
#include <bits/stdc++.h>

using namespace std;

class Solution {
    int n;
    int m;
    public:

    void dfs(vector<vector<int>>& heights, vector<vector<bool>>& flag, int i, int j){

        flag[i][j] = true;
        if ( i > 0 && !flag[i-1][j] && heights[i][j] <= heights[i-1][j] ) {
            dfs(heights, flag, i-1, j);
        }
        if ( j > 0 && !flag[i][j-1] && heights[i][j] <= heights[i-1][j-1] ) {
            dfs(heights, flag, i, j-1);
        }
        if ( i < n-1 && !flag[i+1][j] && heights[i][j] <= heights[i+1][j] ) {
            dfs(heights, flag, i+1, j);
        }
        if ( j < m-1 && !flag[i][j-1] && heights[i][j] <= heights[i][j-1] ) {
            dfs(heights, flag, i, j-1);
        }
    }

    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        n = heights.size();
        m = heights[0].size();

        vector<vector<bool>> atl(n, vector<bool>(m, false));
        vector<vector<bool>> pac(n, vector<bool>(m, false));
        vector<vector<int>> ans;

        for (int i=0; i<n; i++) {
            dfs(heights, pac, i, 0);
            dfs(heights, atl, n-1, i);
        }
        for (int i=0; i<m; i++) {
            dfs(heights, pac, 0, i);
            dfs(heights, atl, m-1, i);
        }

        for (int i=0; i<n; i++)  {
            for (int j=0; j<n; j++) {
                if (pac[i][j] && atl[i][j]) {
                    ans.push_back({i, j});
                }
            }
        }
        return ans;
    }
};
