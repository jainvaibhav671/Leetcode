
from typing import List


class Solution:

    def dfs(self, curr, graph, visited):
        if visited[curr]:
            return 0

        count = 1
        visited[curr] = True

        for _next in graph[curr]:
            count += self.dfs(_next, graph, visited)

        return count

    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        graph = [[] for _ in range(n)]
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        visited = [False] * n
        count = 0
        already_counted = 0
        for i in range(n):
            if not visited[i]:
                cnt = self.dfs(i, graph, visited)
                already_counted += cnt
                count += cnt * (n - already_counted)
        return count

        return count
