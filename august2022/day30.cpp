
#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
    void rotate(vector<vector<int>>& matrix) {
        int left = 0;
        int right = matrix.size() - 1;

        while (left < right) {
            for (int i=0; i<right; i++) {
                int top = left;
                int bottom = right;
                int topRight = matrix[top+i][right];
                matrix[top+i][right] = matrix[top][left+i];
                matrix[top][left+i] = matrix[bottom-i][right];
                matrix[bottom-i][right] = matrix[bottom][right-i];
                matrix[bottom][right-i] = topRight;
            }
            left++;
            right--;
        }
    }
};
