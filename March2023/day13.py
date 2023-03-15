from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, left: Optional[TreeNode], right: Optional[TreeNode]):
        if not left and not right:
            return True
        elif not left or not right:
            return False

        if left.val != right.val:
            return False

        _left = self.traverse(left.right, right.left)
        _right = self.traverse(left.left, right.right)

        if _left and _right:
            return True

        return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root.left, root.right)
