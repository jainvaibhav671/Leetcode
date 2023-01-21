
# https://leetcode.com/problems/restore-ip-addresses

class Solution:
    def isValid(self, string: str) -> bool:
        n: int = len(string)
        if n > 3 or n == 0:
            return False
        if n > 1 and string[0] == '0':
            return False
        if n and int(string) > 255:
            return False
        return True

    def solve(self, ans, output, ind, s, dots):
        if dots == 3:
            if self.isValid(s[ind:]):
                ans.append(output + s[ind:])
            return
        for i in range(ind, min(ind+3, len(s))):
            if self.isValid(s[ind:i+1]):
                new_output = output + s[ind:i+1] + '.'
                self.solve(ans, new_output, i+1, s, dots+1)

    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.solve(ans, "", 0, s, 0)
        return ans
