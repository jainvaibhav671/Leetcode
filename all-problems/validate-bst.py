
# https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def inorderTraversal(self, root, elems):
        if not root:
            return
        
        self.inorderTraversal(root.left, elems)
        elems.append(root.val)
        self.inorderTraversal(root.right, elems)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        elems: List[int] = []
        self.inorderTraversal(root, elems)

        for i in range(1, len(elems)):
            if elems[i-1] >= elems[i]:
                return False
        return True
