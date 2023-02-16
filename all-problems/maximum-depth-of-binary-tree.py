
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth: int = -1

        queue: List[Tuple[Optional[TreeNode], int]] = [(root, 1)]
        while queue:
            curr, depth = queue.pop(0)
            
            # leaf node
            if not curr.left and not curr.right:
                max_depth = max(max_depth, depth)
                continue
            
            if curr.left:
                queue.append(( curr.left, depth + 1 ))
            if curr.right:
                queue.append(( curr.right, depth + 1 ))
            
        return max_depth
