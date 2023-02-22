
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days

class Solution {

public:

    int shipWithinDays(vector<int>& weights, int days) {

        int max_weight = -1;

        int total_weight = 0;

        for (auto weight : weights) {

            max_weight = max(max_weight, weight);

            total_weight += weight;

        }



        while (max_weight < total_weight) {

            int average_weight = max_weight + ((total_weight - max_weight) / 2);

            int curr_weight = 0;

            int days_needed = 1;

            for (auto& weight : weights) {

                if (curr_weight + weight > average_weight) {

                    days_needed += 1;

                    curr_weight = 0;

                }

                curr_weight += weight;

            }



            if (days_needed > days) {

                max_weight = average_weight + 1;

            } else {

                total_weight = average_weight;

            }

        }

        return max_weight;

    }

};
