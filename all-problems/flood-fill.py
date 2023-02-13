
# https://leetcode.com/problems/flood-fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image
        
        n: int = len(image[0])
        m: int = len(image)
        queue: List[Tuple[int, int]] = [ (sr,sc) ]
        dirs: List[Tuple[int, int]] = [ (0,1), (1,0), (-1,0), (0,-1) ]
        while queue:
            x, y = queue.pop(0)
            for dx,dy in dirs:
                i, j = x+dx, y+dy
                if i < 0 or j < 0 or i >= m or j >= n:
                    continue
                
                if image[i][j] == image[x][y] and (i,j) not in queue:
                    queue.append((i,j))
            image[x][y] = color

        return image

            

