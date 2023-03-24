
from typing import List


class Solution:

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] * n for _ in range(n)]

        for src, dst in connections:
            graph[src].append((dst, 1))
            graph[dst].append((src, 0))

        min_operations = 0
        q = [0]
        visited = [False] * n
        visited[0] = True
        while q:
            curr = q.pop(0)
            for neighbor, direction in graph[curr]:
                if visited[neighbor]:
                    continue

                visited[neighbor] = True
                min_operations += direction
                q.append(neighbor)

        return min_operations
