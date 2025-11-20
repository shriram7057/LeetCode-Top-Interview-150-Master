class Solution(object):
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                up = grid[i - 1][j] if i > 0 else float('inf')
                left = grid[i][j - 1] if j > 0 else float('inf')
                grid[i][j] += min(up, left)
        return grid[m - 1][n - 1]
