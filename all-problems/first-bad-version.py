#!/usr/bin/env python3

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# https://leetcode.com/problems/first-bad-version


class Solution:
    def firstBadVersion(self, n: int) -> int:
        i = 0
        j = n

        first = j
        while i <= j:
            mid = i + int((j - i) / 2)
            if isBadVersion(mid):
                first = mid
                j = mid - 1
            else:
                i = mid + 1
        return first
