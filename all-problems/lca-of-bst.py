
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.lca: Optional[TreeNode] = TreeNode(1e8)

    def helper(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> None:
        if not root:
            return None
        
        if p.val < root.val and q.val < root.val:
            if root.val < self.lca.val: self.lca = root
            self.helper(root.left, p, q)
        
        elif q.val > root.val and p.val > root.val:
            if root.val < self.lca.val: self.lca = root
            self.helper(root.right, p, q)

        else:
            self.lca = root

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.helper(root, p, q)
        return self.lca

        
        
