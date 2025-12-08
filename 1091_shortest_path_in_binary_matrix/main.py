from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid) # == len(grid[0])

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        # Edge case: if the grid is 1x1 and path isn't blocked, path is 1
        if n == 1:
            return 1

        # The problem provides us with a 2D grid, and asks us to, starting from (0,0),
        # find the shortest path through the grid to the point (n-1,n-1).

        # We'll model the grid cells as nodes with 8-direction edges, and we'll use
        # BFS to find the shortest path through the grid.

        # BFS uses a queue as its traversal method. Init a deque to use as our queue
        q = deque()

        # We store a nxn binary matrix to represent our visited state
        # To not confuse myself, I'll init the visited state as 1
        visited = [[1] * n for _ in range(n)]

        def visit(r, c):
            visited[r][c] = 0
        
        def isNotVisited(r, c) -> bool:
            return not visited[r][c] == 0

        def isOnPath(r, c) -> bool:
            return grid[r][c] == 0
        
        def isInBounds(r, c):
            return 0 <= r < n and 0 <= c < n

        def neighbors8(r,c):
            n8 = []
            for dr in range(-1,2):
                for dc in range(-1,2):
                    if dr == 0 and dc == 0:
                        continue

                    possibleNeighborR = r+dr
                    possibleNeighborC = c+dc

                    if isInBounds(possibleNeighborR, possibleNeighborC) and isOnPath(possibleNeighborR, possibleNeighborC):
                        n8.append((possibleNeighborR,possibleNeighborC))
            
            return n8

        # Step 1 of BFS algo is to push *a* vertex onto the queue.
        q.append((0,0,1)) # Represent cell as a 3-tuple with 3 being path length

        # The path length is per row that we visit, if we orient the graph at (0,0)

        while len(q) > 0:
            r, c, distance = q.popleft()
            if r == n-1 and c == n-1:
                return distance

            if isNotVisited(r, c):
                visit(r, c)
                
                # Add adjacent nodes into queue (8 directions)
                for neighbor in neighbors8(r,c):
                    nr, nc = neighbor
                    q.append((nr, nc, distance+1))

        return -1
