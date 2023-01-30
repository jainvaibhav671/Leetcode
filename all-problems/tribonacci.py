
# https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    def tribonacci(self, n: int) -> int:
        """
        Function to return n-th tribonacci number
        Time Complexity: O(n)
        Space Complexity: O(n)

        a_n = a_n-1 + a_n-2 + a_n-3

        """

        if n == 0:
            return 0
        if n <= 2:
            return 1
        memo = [-1] * (n+1)
        memo[0] = 0
        memo[1] = memo[2] = 1

        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        
        return memo[n]
