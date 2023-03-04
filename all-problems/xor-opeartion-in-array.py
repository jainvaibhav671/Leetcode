class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums: List[int] = [start + 2 * i for i in range(n)]
        xor: int = functools.reduce(lambda x, y: x ^ y, nums)
        return xor
