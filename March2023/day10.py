
from typing import Optional
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.len: int = 0
        while head:
            self.len += 1
            head = head.next       

    def getRandom(self) -> int:
        ind: int = random.randint(0, self.len - 1)

        tmp_head: Optional[ListNode] = self.head
        while tmp_head:
            if ind == 0:
                return tmp_head.val
            ind -= 1
            tmp_head = tmp_head.next
        return 0


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()