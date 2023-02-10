#!/usr/bin/env python3

# https://leetcode.com/problems/longest-palindrome


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for ch in s:
            count.setdefault(ch, 0)
            count[ch] += 1

        length = 0
        for ch in s:
            if count[ch] % 2 == 0:
                length += count[ch]
                count[ch] = 0
            else:
                if length % 2 == 0:
                    length += 1
                    count[ch] -= 1

                length += count[ch] // 2 * 2
                count[ch] = 0

        return length
