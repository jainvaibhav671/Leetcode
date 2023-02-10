
// https://leetcode.com/problems/naming-a-company

class Solution {
public:
    long long distinctNames(vector<string>& ideas) {
        set<string> sets[26];
        for (auto& idea : ideas) sets[idea[0] - 'a'].insert(idea.substr(1));

        vector<vector<int>> same(26, vector<int>(26, 0));

        for (int i=0; i<26; i++) {
            for (auto& s : sets[i]) {
                for (int j=i+1; j<26; j++) {
                    if (sets[j].find(s) != sets[j].end()) {
                        same[i][j]++;
                    }
                }
            }
        }

        long res = 0;
        for (int i=0; i<26; i++) {
            for (int j=i+1; j<26; j++) {
                res += (sets[i].size() - same[i][j]) * (sets[j].size() - same[i][j]) * 2;
            }
        }
        return res;
    }
};
