
// https://leetcode.com/problems/valid-sudoku

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int len = 9;

        // check rows and cols
        for (int i=0; i<len; i++) {
            vector<bool> freq_row(10, false);
            vector<bool> freq_col(10, false);
            for (int j=0; j<len; j++) {
                char r = board[i][j];
                char c = board[j][i];
                if (r != '.') {
                    if (freq_row[r - '0']) return false;
                    freq_row[r - '0'] = true;
                }
                if (c != '.') {
                    if (freq_col[c - '0']) return false;
                    freq_col[c - '0'] = true;
                }
            }
        }

        // check grids
        for (int i=0; i<len; i+=3) {
            for (int j=0; j<len; j+=3) {
                vector<bool> freq(10, false);
                for (int x=0; x<3; x++) {
                    for (int y=0; y<3; y++) {
                        char k = board[i+x][j+y];
                        if (k == '.') continue;
                        if (freq[k - '0']) return false;
                        freq[k - '0'] = true;
                    }
                }
            }
        }
        return true;
    }
};
