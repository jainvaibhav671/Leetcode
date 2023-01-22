
# https://leetcode.com/problems/palindrome-partitioning

class Solution:

    def __init__(self):
        self.ans: List[List[str]] = []
        self.currList: List[str] = []

    def isPalindrome(self, s: str, low: int, high: int):
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        
        def dfs(s: str, start: int):
            if start >= len(s):
                self.ans.append(self.currList.copy())
            
            for end in range(start, len(s)):
                if self.isPalindrome(s, start, end):
                    self.currList.append(s[start:end+1])
                    dfs(s, end+1)
                    self.currList.pop()
                    
        dfs(s, 0)
        
        return self.ans
