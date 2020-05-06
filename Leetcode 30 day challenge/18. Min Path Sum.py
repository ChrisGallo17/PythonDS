'''
class Solution:
    def minPathSum(self, grid):
        if grid == []:
            return 0

        ans = []
        for i in range(len(grid)):
            ans.append([])
            for j in range(len(grid[i])):
                ans[i].append(None)

        self.dfs(grid, 0, 0, None, ans)
        return ans[len(grid) - 1][len(grid[0]) - 1]

    def dfs(self, grid, i, j, prevSum=None, ans=[]):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
            return 0

        if ans[i][j] is None:
            if prevSum is None:
                prevSum = grid[i][j]
                ans[i][j] = prevSum
            else:
                ans[i][j] = prevSum + grid[i][j]
        else:
            if ans[i][j] > grid[i][j] + prevSum:
                ans[i][j] = grid[i][j] + prevSum
            else:
                return 0

        self.dfs(grid, i, j + 1, ans[i][j], ans)
        self.dfs(grid, i + 1, j, ans[i][j], ans)

s = Solution()
print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
'''

class Solution:
    def minPathSum(self, grid):
        if grid == [] or grid is None:
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    continue
                if i - 1 < 0: # top of grid
                   grid[i][j] = grid[i][j] + grid[i][j - 1]
                elif j - 1 < 0:  # left of grid
                   grid[i][j] = grid[i][j] + grid[i - 1][j]
                else: # everything else
                    grid[i][j] = grid[i][j] + min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]

s = Solution()
print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
