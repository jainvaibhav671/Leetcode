
// link : https://leetcode.com/problems/sort-the-matrix-diagonally

#include <vector>
#include <algorithm>

using namespace std;

class Solution {
      public:
      void sortDiagonal(vector<vector<int>>& mat, int i, int j) {
            vector<int> elems;
            int x = i;
            int y = j;
            while (x < mat.size() && y < mat[0].size()) {
                  elems.push_back( mat[x++][y++] );
            }

            sort(elems.begin(), elems.end());
            x = i;
            y = j;
            for (int k=0; k<elems.size(); k++) {
                  mat[x++][y++] = elems[k];
            }
      }

      vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
            // row = 0;
            for (int col=0; col<mat[0].size(); col++) {
                  sortDiagonal(mat, 0, col);
            }

            // col = 0
            for (int row=0; row<mat[0].size(); row++) {
                  sortDiagonal(mat, row, 0);
            }
            return mat;
      }
};
