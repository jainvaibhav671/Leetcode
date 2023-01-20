# https://leetcode.com/problems/non-decreasing-subsequences/submissions/881995631/


class Solution:
    def __init__(self):
        self.ans: set = set()

    def backtrack(self, nums: List[int], ind: int = 0, seq: List[int] = []):

        resSeq: List[int] = list(map(lambda x: nums[x], seq)).copy()
        if len(seq) >= 2:
            self.ans.add(tuple(resSeq))

        if ind >= len(nums):
            return

        if not seq or nums[ind] >= nums[seq[-1]]:
            seq.append(ind)
            self.backtrack(nums, ind + 1, seq)
            seq.pop()

        self.backtrack(nums, ind + 1, seq)

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, 0, [])
        return self.ans
