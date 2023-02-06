
# https://leetcode.com/problems/shuffle-the-array

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_list: List[int] = []
        i = 0
        j = n

        while True:
            new_list.extend([nums[i], nums[j]])
            i += 1
            j += 1

            if i == n or j == 2*n:
                break
        nums = new_list
        return nums
