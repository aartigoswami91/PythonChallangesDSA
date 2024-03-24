from typing import List


class NoOfIlands:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0


        def dfs(grid,row,col):

            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0':
                return

           #dfs()
           #Change current element to water
            grid[row][col] = '0'

           # Traverse its connected elements
           #Left
            dfs(grid, row, col-1)

           #Right
            dfs(grid, row, col+1)

           #Top
            dfs(grid, row-1, col)

           #Bottom
            dfs(grid, row+1, col)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    result += 1
                    #visit all the conected land
                    dfs(grid,row,col)



        return result



iland = NoOfIlands()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(iland.numIslands(grid))





        