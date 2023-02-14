# https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n: int = max(len(num1), len(num2))

        num1 = num1.rjust(n, '0')
        num2 = num2.rjust(n, '0')

        res: str = ""
        i: int = n - 1
        carry: int = 0

        while i >= 0:
            dig1: int = int(num1[i])
            dig2: int = int(num2[i])

            s = dig1 + dig2 + carry
            digit, carry = s % 10, s // 10
            res = f"{digit}" + res
            i -= 1
        
        if carry != 0:
            res = f"{carry}" + res
        
        return res

