
# https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n: int = len(nums)

        def search(start, end):
            # print(nums[start:end+1], start, end)
            if start < 0 or end >= n or start > end:
                return None

            mid = start + (end - start) // 2
            if mid-1 >= start and nums[mid] == nums[mid-1]:
                res_left = search(start, mid-2)
                if res_left != None:
                    return res_left

                res_right = search(mid+1, end)
                if res_right != None:
                    return res_right
            
            elif mid+1 <= end and nums[mid] == nums[mid + 1]:
                res_left = search(start, mid-1)
                if res_left != None:
                    return res_left
                res_right = search(mid + 2, end)
                if res_right != None:
                    return res_right
            else:
                # print(mid)
                return mid

        return nums[search(0, n-1)]


