# https://leetcode.com/problems/linked-list-cycle-ii

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        nodes = {}
        tmp = head
        while tmp:
            hsh = hash(tmp)
            if nodes.get(hsh, False):
                return tmp

            nodes[hsh] = True
            tmp = tmp.next
        return None
