from typing import List


class Solution:
    def findNext(self, arr: List[int], i: int, target: int) -> List[int]:
        _next: List[int] = []
        cnt = arr.count(target)
        if cnt == 1:
            return []

        for j in range(len(arr)):
            if cnt == 0:
                break

            if arr[j] == target and j != i:
                _next.append(j)
                cnt -= 1

        return _next

    def minJumps(self, arr: List[int]) -> int:
        n: int = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = [0]
        visited = {0}
        min_steps = 0
        while curs:
            _next = []
            for node in curs:
                if node == n - 1:
                    return min_steps

                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        _next.append(child)

                graph[arr[node]].clear()

                for child in [node - 1, node + 1]:
                    if 0 <= child <= n and child not in visited:
                        visited.add(child)
                        _next.append(child)

            curs = _next
            min_steps += 1
        return -1
