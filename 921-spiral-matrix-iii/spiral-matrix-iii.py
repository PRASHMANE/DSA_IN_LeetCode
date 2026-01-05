class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        
        # Directions: Right, Down, Left, Up
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        r, c = rStart, cStart
        result.append([r, c])
        
        steps = 1  # number of moves in one direction
        total = rows * cols
        
        while len(result) < total:
            for i in range(4):
                dr, dc = directions[i]
                
                for _ in range(steps):
                    r += dr
                    c += dc
                    
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                        
                # increase step after every 2 directions
                if i % 2 == 1:
                    steps += 1
                    
        return result