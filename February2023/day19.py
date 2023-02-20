
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        lr: bool = True
        queue = [root, None]
        level = []
        ans = []

        while queue:
            node = queue.pop(0)
            if not node:
                if lr:
                    ans.append(level.copy())
                else:
                    ans.append(level[::-1])
                
                level.clear()
                lr = not lr
                

                if not queue:
                    break

                queue.append(None)
                continue
            
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return ans
