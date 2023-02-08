#!/usr/bin/env python3

# https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp: ListNode = head
        l: int = 0
        while tmp != None:
            l += 1
            tmp = tmp.next

        for i in range(l // 2):
            head = head.next

        return head
