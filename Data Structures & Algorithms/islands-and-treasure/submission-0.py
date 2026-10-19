from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        numRows = len(grid)
        numCols = len(grid[0])

        queue = deque()

        for row in range(numRows):
            for col in range(numCols):
                if grid[row][col] == 0:
                    queue.append([row, col])
        
        moves = [[1,0], [-1, 0], [0, 1], [0, -1]]

        while queue:
            row, col = queue.popleft()
            for dir_row, dir_col in moves:
                nr = dir_row + row
                nc = dir_col + col

                if 0 <= nr < numRows and 0 <= nc < numCols and grid[nr][nc] == inf:
                    grid[nr][nc] = grid[row][col] + 1
                    queue.append([nr, nc])


        