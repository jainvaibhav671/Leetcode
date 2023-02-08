#!/usr/bin/env python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/reverse-linked-list


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        nodes = []
        node_cnt = 0
        while head:
            node_cnt += 1
            nodes.append(head)
            head = head.next
            nodes[-1].next = None

        for i in range(1, node_cnt):
            nodes[i].next = nodes[i - 1]

        return nodes[-1]
