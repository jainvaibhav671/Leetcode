
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def make_tree(self, vals: List[int], s: int, e: int) -> Optional[TreeNode]:
        if s > e:
            return None

        mid: int = s + (e - s) // 2        
        node: Optional[TreeNode] = TreeNode(vals[mid])

        node.left = self.make_tree(vals, s, mid-1)
        node.right = self.make_tree(vals, mid+1, e)

        return node

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        vals: List[int] = []
        while head:
            vals.append(head.val)
            head = head.next

        return self.make_tree(vals, 0, len(vals) - 1)
