
# https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        nodes = {}
        tmp = head
        while tmp:
            hsh = hash(tmp)
            if nodes.get(hsh, False):
                return True
            
            nodes[hsh] = True
            tmp = tmp.next
        return False
