from typing import List


class Solution:
    def countBits(self, num: int) -> int:
        return bin(num).count("1")

    def sortByBits(self, arr: List[int]) -> List[int]:
        n: int = len(arr)
        for i in range(n):
            check: bool = False
            first = i
            for j in range(i, n):
                if self.countBits(arr[j]) < self.countBits(arr[first]):
                    first = j
                    check = True
                elif (
                    self.countBits(arr[j]) == self.countBits(arr[first])
                    and arr[j] < arr[first]
                ):
                    first = j
                    check = True

            arr[i], arr[first] = arr[first], arr[i]
        return arr
