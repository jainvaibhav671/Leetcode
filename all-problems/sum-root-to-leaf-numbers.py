from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, root: Optional[TreeNode], num: str, total_sum: int) -> int:
        if not root:
            return total_sum

        num += f"{root.val}"

        if not root.left and not root.right:
            total_sum += int(num)
        else:
            total_sum = self.traverse(root.left, num, total_sum)
            total_sum = self.traverse(root.right, num, total_sum)

        return total_sum

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.traverse(root, "", 0)
