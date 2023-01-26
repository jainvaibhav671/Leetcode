# https://leetcode.com/problems/cheapest-flights-within-k-stops

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        dp = [ [sys.maxsize for _ in range(k+2)] for _ in range(n+1) ]
        for i in range(k+2):
            dp[src][i] = 0
        
        for i in range(1, k+2):
            for f in flights:
                if dp[f[0]][i-1] != sys.maxsize:
                    dp[f[1]][i] = min(dp[f[1]][i], dp[f[0]][i-1]+ f[2])
        return dp[dst][k+1] if dp[dst][k+1] != sys.maxsize else -1
