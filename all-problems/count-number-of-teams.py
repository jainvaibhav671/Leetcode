from typing import List


class Solution:
    def numTeams(self, nums: List[int]) -> int:
        cnt: int = 0
        n: int = len(nums)

        for i, v in enumerate(nums):
            llc = lgc = rlc = rgc = 0

            for l in nums[:i]:
                if l < v:
                    llc += 1
                else:
                    lgc += 1

            for r in nums[i + 1 :]:
                if r < v:
                    rlc += 1
                else:
                    rgc += 1

            cnt += llc * rgc
            cnt += lgc * rlc

        return cnt
