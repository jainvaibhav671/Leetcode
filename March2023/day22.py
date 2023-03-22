
from typing import List, Tuple, Set, Dict


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        graph: Dict[int, Set[Tuple[int, int]]] = {}
        for src, dest, dist in roads:
            graph.setdefault(src, set())
            graph.setdefault(dest, set())

            graph[src].add((dest, dist))
            graph[dest].add((src, dist))

        network: Set[int] = set()
        q: List[int] = [1]
        min_score: int = 1e9
        # Find Cities connected to 1 and n
        while q:
            curr = q.pop(0)
            if curr in network:
                continue

            network.add(curr)
            for dest, dist in graph[curr]:
                if dest in network:
                    continue

                min_score = min(min_score, dist)
                q.append(dest)
        return min_score
