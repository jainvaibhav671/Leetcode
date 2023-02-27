
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.helper(grid, 0, 0, len(grid))

    def helper(self, grid, i, j, w):
        if self.allSame(grid, i, j, w):
            return Node(grid[i][j] == 1, True, None, None, None, None)
        
        w2 = w // 2
        node = Node(
            True,
            False,
            self.helper(grid, i, j, w2),
            self.helper(grid, i, j + w2, w2),
            self.helper(grid, i + w2, j, w2),
            self.helper(grid, i + w2, j + w2, w2)
        )

        return node
    
    def allSame(self, grid, i, j, w):
        for x in range(i, i+w):
            for y in range(j, j + w):
                if grid[x][y] != grid[i][j]:
                    return False
        return True
