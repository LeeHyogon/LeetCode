class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """



        m = len(heights)
        n = len(heights[0])

        def isPacific (y, x) :
            if (0<=y <=m) and (x ==0):
                return True
            if (0<=x <=n+1) and y ==0:
                return True
            return False
        
        def isAtlantic (y, x) :
            if (1 <= y <=m+1)  and x == n+1:
                return True
            if (0 <= x <=n+1)  and y == m+1:
                return True
            return False

        dy = [0,1,0,-1]
        dx = [-1,0,1,0]
        TARGET_P = 1 << 0
        TARGET_A = 1 << 1

        ans =[]
        isBoth = [[0]*(n+2) for _ in range(m+2)]

        def dfs (y, x,visited):
            state = 0
            if isBoth[y][x] !=0:
                return isBoth[y][x]

            for dir in range(4):
                ny = y +dy[dir]
                nx = x +dx[dir]
                if (0<= ny<=m+1) and (0<= nx<=n+1):
                    if isBoth[y][x] !=0:
                        return isBoth[y][x]
                    if (1 <=ny <=m) and (1<=nx<=n) and (visited[ny][nx]==0):
                        if heights[ny-1][nx-1]<= heights[y-1][x-1]:
                            visited[ny][nx] = 1
                            state |= dfs(ny,nx,visited)
                            visited[ny][nx] = 0
                            if state == (TARGET_P | TARGET_A):
                                return state
                    elif (ny ==0 or ny ==m+1 or nx== 0 or nx == n+1) and (visited[ny][nx]==0):
                        if isPacific(ny,nx) is True:
                            state |= TARGET_P
                        if isAtlantic(ny,nx) is True:
                            state |= TARGET_A
            return state

        for i in range(m):
            for j in range(n):
                visited = [[0]*(n+2) for _ in range(m+2)]
                visited[i+1][j+1] = 1
                ret = dfs(i+1, j+1 ,visited)
                if ret == (TARGET_P | TARGET_A):
                    ans.append([i,j])
                    isBoth[i+1][j+1] = (TARGET_P | TARGET_A)
        return ans