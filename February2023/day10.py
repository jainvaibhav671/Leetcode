#!/usr/bin/env python3

# https://leetcode.com/problems/as-far-from-land-as-possible


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n: int = len(grid)
        queue = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))

        if not queue or len(queue) == n * n:
            return -1

        dist = -1
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            dist += 1
            size = len(queue)
            while size:
                size -= 1
                x, y = queue.pop(0)
                for dx, dy in dirs:
                    i, j = x + dx, y + dy
                    if 0 <= i < n and 0 <= j < n and grid[i][j] == 0:
                        grid[i][j] = 1
                        queue.append((i, j))
        return dist
