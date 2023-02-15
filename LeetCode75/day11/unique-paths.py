
# https://leetcode.com/problems/unique-paths/

class Solution:

    def dfs(self, m: int,  n: int, pos: Tuple[int, int], dp: Dict[Tuple[int, int], bool]) -> int:
        if pos == (m-1, n-1):
            return 1
        elif dp.get(pos, -1) != -1:
            return dp[pos]

        paths: int = 0
        x, y = pos
        right: Tuple[int, int] = (x,  y + 1)
        down: Tuple[int, int] = (x + 1, y)

        for i,j in [right, down]:
            if i >= m or j >= n:
                continue
            paths += self.dfs(m, n, (i, j), dp)
        dp[pos] = paths
        return dp[pos]
            
    def uniquePaths(self, m: int, n: int) -> int:
        dp: Dict[Tuple[int, int], int] = {}
        pos: Tuple[int, int] = (0, 0)

        return self.dfs(m, n, pos, dp)
