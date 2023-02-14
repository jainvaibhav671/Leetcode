
# https://leetcode.com/problems/add-to-array-form-of-integer

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry: int = 0
        i: int = len(num) - 1
        while k and i >= 0:
            dig1 = k % 10
            k //= 10

            dig2 = num[i]
            s: int = dig1 + dig2 + carry

            digit, carry = s % 10, s // 10
            num[i] = digit
            i -= 1
        
        while k:
            dig = k % 10
            k //= 10

            s: int = dig + carry
            dig, carry = s % 10, s // 10
            num.insert(0, dig)
        
        while i >= 0:
            dig = num[i]
            s: int = dig + carry
            dig, carry = s % 10, s // 10
            num[i] = dig
            i -= 1
        
        if carry != 0:
            num.insert(0, carry)
        
        return num



