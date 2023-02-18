
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

class Solution:

    def preorder(self, root: Optional[TreeNode], elems: List[int]):
        if not root:
            return
        
        elems.append(root.val)
        self.preorder(root.left, elems)
        self.preorder(root.right, elems)

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        elems: List[int] = []
        self.preorder(root, elems)
        
        min_diff: int = 1e8
        n: int = len(elems)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                
                min_diff = min(min_diff, abs(elems[i] - elems[j]))
        return min_diff
