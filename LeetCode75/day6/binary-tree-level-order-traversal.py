
# Definition for a binary tree node.

# https://leetcode.com/problems/binary-tree-level-order-traversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        ans: List[List[int]] = []
        level: List[int] = []
        queue: List[Optional[TreeNode]] = [root, None]

        while queue:
            front = queue.pop(0)
            if front != None:
                level.append(front.val)
                if front.left:
                    queue.append(front.left)
                
                if front.right:
                    queue.append(front.right)
                
            elif queue:
                ans.append(level.copy())
                level.clear()
                queue.append(None)
        
        ans.append(level)
        return ans
