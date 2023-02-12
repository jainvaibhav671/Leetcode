#!/usr/bin/env python3

# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital


class Solution:
    def __init__(self):
        self.ans = 0

    def dfs(self, pos, adj, vis, seats):
        vis[pos] = True
        count = 1

        for dest in adj[pos]:
            if vis[dest]:
                continue
            count += self.dfs(dest, adj, vis, seats)

        x = count // seats
        if count % seats:
            x += 1
        if pos != 0:
            self.ans += x

        return count

    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads)

        adj = [[] for _ in range(n + 1)]
        vis = [False] * (n + 1)
        for s, d in roads:
            adj[s].append(d)
            adj[d].append(s)

        self.dfs(0, adj, vis, seats)
        return self.ans
