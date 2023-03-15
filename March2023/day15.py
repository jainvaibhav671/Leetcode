
from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        null: bool = False

        nodes: List[Optional[TreeNode]] = [root]

        while nodes:
            front: Optional[TreeNode] = nodes.pop(0)
            if not front:
                null = True
                continue

            if null:
                return False

            nodes.extend([front.left, front.right])

        return True
