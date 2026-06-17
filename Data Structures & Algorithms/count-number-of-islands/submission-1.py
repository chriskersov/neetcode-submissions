class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and ((i, j) not in islands):
                    islands.append(self.dfs(grid, i, j, set(), set()))
        result = []
        for island in islands:
            if island not in result:
                result.append(island)
        return len(result)   

    def dfs(self, grid, r, c, visit, island):
        rows = len(grid)
        columns = len(grid[0])
        if (r < 0) or (c < 0) or (r == rows) or (c == columns) or (grid[r][c] == '0') or ((r, c) in visit):
            return
        if (grid[r][c] == '1'):
            island.add((r, c))
        visit.add((r, c))
        self.dfs(grid, r + 1, c, visit, island)
        self.dfs(grid, r - 1, c, visit, island)
        self.dfs(grid, r, c + 1, visit, island)
        self.dfs(grid, r, c - 1, visit, island)
        return island
