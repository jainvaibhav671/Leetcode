
# https://leetcode.com/problems/find-the-town-judge

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        l = [0]*(n+1)
        for a,b in trust:
            l[b] += 1
            l[a] -= 1

        for i in range(1, n+1):
            if l[i] == n-1:
                return i
        return -1
