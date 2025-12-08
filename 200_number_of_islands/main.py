class Solution(object):
    visited = [[]]

    def numIslands(self, grid) -> int:
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        # We don't check if grid is empty per the constraints
        numIslands = 0

        rows = len(grid)
        cols = len(grid[0]) # Grid is m x n; 0th index will give us the # of cols

        self.visited = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if self.isLand(grid, row, col) and not self.isVisited(row, col):
                    numIslands = numIslands + 1
                    self.explore(grid, row, col)

        return numIslands

    def isLand(self, grid, row, col) -> bool:
        return self.inBounds(grid, row, col) and grid[row][col] == "1"

    def inBounds(self, grid, row, col) -> bool:
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    def isVisited(self, row, col) -> bool:
        return self.visited[row][col] == 1

    def markVisited(self, row, col):
        self.visited[row][col] = 1

    def neighbors4(self, row, col):
        return [(row-1, col),(row+1, col),(row,col-1),(row,col+1)]
    
    def explore(self, grid, row, col):
        stack = []
        stack.append((row, col)) # Push the 'root' of the graph onto the stack

        while len(stack) > 0:
            r, c = stack.pop()
            # Spread the contents of this across args of helper
            if self.inBounds(grid, r, c) and self.isLand(grid, r, c) and not self.isVisited(r, c):
                self.markVisited(r, c)
                n4 = self.neighbors4(r, c)
                for n in n4:
                    if self.inBounds(grid, *n) and self.isLand(grid, *n):
                        stack.append(n)


solution = Solution()

grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(solution.numIslands(grid1))

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(solution.numIslands(grid2))
