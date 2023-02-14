
# https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = False
        na: int = len(a)
        nb: int = len(b)

        if na > nb:
            diff = na - nb
            b = "0" * diff + b
        else:
            diff = nb - na
            a = "0" * diff + a

        i: int = len(a) - 1
        j: int = len(b) - 1

        res = ""
        print(a, b)

        while i >= 0 and j >= 0:
            ci = a[i]
            cj = b[j]

            add = ''
            if ci == '1' and cj == '1':
                add = '1' if carry else '0'
                carry = True
            elif ci == '0' and cj == '0':
                if carry:
                    carry = False
                    add = '1'
                else:
                    add = '0'
            else:
                add = '0' if carry else '1'

            i -= 1
            j -= 1
            res = add + res
        if carry:
            res = "1" + res
        return res
