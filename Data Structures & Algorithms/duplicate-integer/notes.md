# Contains Duplicate

## Approach
Use a set to keep track of numbers we have already seen.  
Loop through the array, and if a number is already in the set, return `True`.  
If the loop finishes without finding a duplicate, return `False`.

## Complexity
Time: O(n), because we check each number once.  
Space: O(n), because the set can store up to every number in the input.
