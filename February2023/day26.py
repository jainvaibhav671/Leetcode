
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n1: int = len(word1)
        n2: int = len(word2)
        dp: List[List[int]] = [[-1 for x in range(n2+1)] for y in range(n1+1)]

        def lev(i: int, j: int) -> int:
            nonlocal dp

            if i == 0:
                return j
            elif j == 0:
                return i

            elif dp[i][j] != -1:
                return dp[i][j]
            
            operations: int = 0
            if word1[i-1] == word2[j-1]:
                operations = lev(i-1, j-1)
            else:
                operations = 1 + min([
                    lev(i, j-1),
                    lev(i-1, j),
                    lev(i-1, j-1)
                ])
            dp[i][j] = operations
            return operations

        return lev(n1, n2)
        
