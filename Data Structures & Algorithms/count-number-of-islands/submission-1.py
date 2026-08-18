class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        visit = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))

            directions = [
                (0, 1),   # right
                (0, -1),  # left
                (1, 0),   # down
                (-1, 0)   # up
            ]

            while q:
                r,c = q.popleft()

                for dr,dc in directions:
                    newRow = r + dr
                    newCol = c + dc

                    if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]):
                        if grid[newRow][newCol] == "1" and (newRow,newCol) not in visit:
                            q.append((newRow,newCol))
                            visit.add((newRow,newCol))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visit:
                    island += 1
                    bfs(r,c)

        return island