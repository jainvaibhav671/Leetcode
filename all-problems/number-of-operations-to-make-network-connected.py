
from typing import List


class Solution:
    def dfs(self, i, graph, visited):
        visited[i] = True
        for neighbor in graph[i]:
            if not visited[neighbor]:
                self.dfs(neighbor, graph, visited)

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1

        graph = [[] for _ in range(n)]
        for src, dst in connections:
            graph[src].append(dst)
            graph[dst].append(src)

        cables_needed = -1
        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue
            cables_needed += 1
            self.dfs(i, graph, visited)

        return cables_needed
