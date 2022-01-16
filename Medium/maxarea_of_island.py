class Solution:
    def fill(self, grid: List[List[int]], i: int, j: int) -> int:
        if(i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!=1):
            return 0
        grid[i][j]=0
        count=1
        count=count+self.fill(grid,i+1,j)
        count=count+self.fill(grid,i-1,j)
        count=count+self.fill(grid,i,j+1)
        count=count+self.fill(grid,i,j-1)
        return count
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        maxcount=0
        for i in range(0,m):
            for j in range(0,n):
                if(grid[i][j]==1):
                    maxcount=max(maxcount,self.fill(grid,i,j))
        return maxcount
    
    '''
    [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    '''
        
        