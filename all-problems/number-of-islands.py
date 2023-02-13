
# https://leetcode.com/problems/number-of-islands

class Solution:

    def bfs(self, grid: List[List[str]], i: int, j: int):
        m: int = len(grid)
        n: int = len(grid[0])
        queue: List[Tuple[int, int]] = [(i,j)]
        dirs: List[Tuple[int, int]] = [ (0, 1), (1,0), (-1,0), (0, -1) ]

        isIsland: bool = False
        while queue:
            x,y = queue.pop(0)
            grid[x][y] = '0'

            water: int = 0
            for dx,dy in dirs:
                i = x + dx
                j = y + dy
                if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
                    water += 1
                elif (i, j) not in queue:
                    queue.append((i, j))
            if water == 4:
                isIsland = True

        return 1 if isIsland else 0


    def numIslands(self, grid: List[List[str]]) -> int:
        m: int = len(grid)
        n: int = len(grid[0])
        cnt: int = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                else:
                    cnt += self.bfs(grid, i, j)
        print()
        return cnt
        
