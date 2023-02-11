#!/usr/bin/env python3

# https://leetcode.com/problems/shortest-path-with-alternating-colors/


class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:

        ans: List[int] = [-1] * n
        graph: List[List[Tuple[int, str]]] = [[] for _ in range(n)]
        queue: List[Tuple[int, str]] = [(0, "i")]

        for u, v in redEdges:
            graph[u].append((v, "r"))
        for u, v in blueEdges:
            graph[u].append((v, "b"))

        dist: int = -1
        while queue:
            q: int = len(queue)
            dist += 1
            for _ in range(q):
                u, prevColor = queue.pop(0)
                if ans[u] == -1:
                    ans[u] = dist

                for i, (v, edgeColor) in enumerate(graph[u]):
                    if v == -1 or edgeColor == prevColor:
                        continue

                    queue.append((v, edgeColor))
                    graph[u][i] = (-1, edgeColor)
        return ans
