# Number of Islands

## Approach
Use BFS to explore each island in the grid.  
Loop through every cell, and whenever we find land `"1"` that has not been visited, we found a new island.

Increase the island count and start BFS from that cell.  
Use a queue to visit all connected land cells in the four directions: right, left, down, and up.  
Add each visited land cell to a set so we do not process it again.

When the BFS finishes, the entire island has been visited.

## Complexity
Time: O(m × n), because every cell in the grid is visited at most once.  
Space: O(m × n), because the visited set and BFS queue can contain cells from the grid.
