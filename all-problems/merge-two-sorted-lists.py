#!/usr/bin/env python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/merge-two-sorted-lists


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        new_list = ListNode()
        tmp = new_list

        while list1 and list2:
            if list1.val <= list2.val:
                tmp.next = list1
                list1 = list1.next
            else:
                tmp.next = list2
                list2 = list2.next
            tmp = tmp.next

        while list1:
            tmp.next = list1
            list1 = list1.next
            tmp = tmp.next
        while list2:
            tmp.next = list2
            list2 = list2.next
            tmp = tmp.next

        return new_list.next
