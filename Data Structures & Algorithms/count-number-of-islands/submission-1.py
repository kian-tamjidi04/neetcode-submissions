class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Update the grid after finding an island
        def dfs(grid, row, col):
            DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            stack = [(row, col)]
            m, n = len(grid), len(grid[0])

            while stack:
                currRow, currCol = stack.pop()

                for (r, c) in DIRS:
                    nextRow, nextCol = r + currRow, c + currCol

                    if 0 <= nextRow < m and 0 <= nextCol < n and grid[nextRow][nextCol] == "1":
                        grid[nextRow][nextCol] = 0
                        stack.append((nextRow, nextCol))
            
            return grid

        islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    grid = dfs(grid, row, col)
                    islands += 1

        return islands
