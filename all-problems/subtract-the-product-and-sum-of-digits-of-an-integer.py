class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod: int = 1
        add: int = 0

        while n:
            dig = n % 10
            prod *= dig
            add += dig
            n = n // 10
        return prod - add
