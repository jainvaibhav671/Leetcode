
# https://leetcode.com/problems/verifying-an-alien-dictionary

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(1, len(words)):
            prev = words[i-1]
            curr = words[i]

            n = min([len(prev), len(curr)])
            substring = False
            for j in range(n):
                prevInd = order.index(prev[j])
                currInd = order.index(curr[j])

                if prevInd > currInd:
                    return False
                elif prevInd < currInd:
                    substring = False
                    break
                else:
                    substring = True
                    continue
            if substring and len(prev) > len(curr):
                return False
        return True
