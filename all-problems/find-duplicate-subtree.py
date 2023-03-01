
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.record: dict = {}
        self.ans: List[Optional[TreeNode]] = []

    def traverse(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        res: str = ""
        if not root.left and not root.right:
            res = f"{root.val}"
        
        else:
            res = f"({self.traverse(root.left)}){root.val}({self.traverse(root.right)})"

        if self.record.get(res, 0) != 0:
            self.record[res] += 1
            if self.record[res] == 2:
                self.ans.append(root)

        else:
            self.record[res] = 1
        
        return res
        

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.traverse(root)
        return self.ans
