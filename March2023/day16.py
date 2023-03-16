from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not inorder or not postorder:
            return None

        head: Optional[TreeNode] = TreeNode(postorder[-1])

        ind: int = inorder.index(head.val)
        head.left = self.buildTree(inorder[:ind], postorder[:ind])
        head.right = self.buildTree(inorder[ind+1:], postorder[ind:-1])

        return head
