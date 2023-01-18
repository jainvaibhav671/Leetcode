
// link : https://www.leetcode.com/problems/number-of-islands

class Solution {
    public:
    bool isIsland(vector<vector<char>>& grid, int i, int j) {

        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size()) return false;

        bool up = true;
        bool down = true;
        bool left = true;
        bool right = true;

        grid[i][j] = '0';

        if (i > 0) {
            if (grid[i-1][j] == '0') up = true;
            else {
                up = isIsland(grid, i-1, j);
            }
        }

        if (j > 0) {
            if (grid[i][j-1] == '0') left = true;
            else {
                left = isIsland(grid, i, j-1);
            }
        }

        if (i < grid.size()-1) {
            if (grid[i+1][j] == '0') down = true;
            else {
                down = isIsland(grid, i+1, j);
            }
        }

        if (j < grid[0].size()-1) {
            if (grid[i][j+1] == '0') right = true;
            else {
                right = isIsland(grid, i, j+1);
            }
        }

        if (up && down && right && left) return true;
        return false;
    }

    int numIslands(vector<vector<char>>& grid) {
        int cnt = 0;
        for (int i=0; i<grid.size(); i++) {
            for (int j=0; j<grid[0].size(); j++) {
                if (grid[i][j] == '1' && isIsland(grid, i, j)) {
                    cnt++;
                }
            }
        }
        return cnt;
    }
};
