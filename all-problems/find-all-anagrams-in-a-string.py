
# https://leetcode.com/problems/find-all-anagrams-in-a-string

class Solution:
    def areEqual(self, a:List[int], b: List[int]) -> bool:
        for i in range(26):
            if a[i] != b[i]:
                return False
        return True

    def findAnagrams(self, s: str, p: str) -> List[int]:
        f1: List[int] = [p.count(chr(i + 97)) for i in range(26)]
        f2: List[int] = [0] * 26

        np: int = len(p)
        ns: int = len(s)
        ans: List[int] = []

        i: int = 0
        j: int = 0
        while j < ns:
            f2[ord(s[j]) - 97] += 1
            if j-i+1 == np:
                if self.areEqual(f1, f2):
                    ans.append(i)
                f2[ord(s[i]) - 97] -= 1
                j += 1
                i += 1
            elif j-i+1 < np:
                j += 1

        return ans
