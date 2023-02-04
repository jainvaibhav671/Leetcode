
# https://leetcode.com/problems/permutation-in-string

class Solution:
    def areEqual(self, a: List[int], b: List[int]) -> bool:
        for i in range(26):
            if a[i] != b[i]:
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        f1: List[int] = [s1.count(chr(97 + i)) for i in range(26)]
        f2: List[int] = [0] * 26

        i: int = 0
        j: int = 0
        while j < len(s2):
            f2[ord(s2[j]) - 97] += 1

            n: int = len(s1)
            if j-i+1 == n and self.areEqual(f1, f2):
                return True
            
            elif j-i+1 < n:
                j += 1
            else:
                f2[ord(s2[i]) - 97] -= 1
                i += 1
                j += 1
        return False
