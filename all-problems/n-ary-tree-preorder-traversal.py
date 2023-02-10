# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def helper(self, root: 'Node', seq: List[int]) -> None:
        if not root:
            return None
        
        seq.append(root.val)
        for child in root.children:
            self.helper(child, seq)

    def preorder(self, root: 'Node') -> List[int]:
        preorder: List[int] = []
        self.helper(root, preorder)
        return preorder

