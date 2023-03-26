
from typing import List, Dict


class Solution:

    def __init__(self):
        self.answer: int = -1

    def dfs(self, curr: int, edges: List[int], visited: List[bool], dist: Dict[int, int]):

        visited[curr] = True
        neighbour: int = edges[curr]
        if neighbour != -1 and not visited[neighbour]:
            dist[neighbour] = dist[curr] + 1
            self.dfs(neighbour, edges, visited, dist)
        elif neighbour != -1 and dist.get(neighbour, None):
            self.answer = max(self.answer, dist[curr] - dist[neighbour] + 1)

    def longestCycle(self, edges: List[int]) -> int:
        n: int = len(edges)
        visited: List[bool] = [False] * n

        for src in range(n):
            if not visited[src]:
                self.dfs(src, edges, visited, {src: 1})

        return self.answer
