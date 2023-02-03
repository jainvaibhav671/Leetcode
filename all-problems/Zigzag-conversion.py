
# https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)

        if 1 == numRows:
            return s

        numCols = n
        grid = [ [""]*numCols for _ in range(numRows)]
        
        row = 0
        col = 0
        down = True

        for ch in s:
            grid[row][col] = ch
            if down:
                row += 1
                if row == numRows-1:
                    down = False
            elif not down:
                row -= 1
                col += 1
                if row == 0:
                    down = True

        return "".join([ "".join(row) for row in grid ])
