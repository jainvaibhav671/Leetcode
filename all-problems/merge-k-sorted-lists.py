
from typing import List, Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        head: Optional[ListNode] = ListNode()
        tail: Optional[ListNode] = head
        while any(lists):
            min_value: int = 1e9
            min_list: int = -1

            for i, ll in enumerate(lists):
                if not ll:
                    continue

                if ll.val < min_value:
                    min_value = ll.val
                    min_list = i

            tail.next = ListNode(min_value)
            lists[min_list] = lists[min_list].next
            tail = tail.next

        return head.next
