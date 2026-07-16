# Two Sum

## Approach
Use a dictionary to store each number and its index.  
For each number, calculate the difference needed to reach the target.  
If that difference is already in the dictionary, return its index and the current index.  
Otherwise, store the current number and its index.

## Complexity
Time: O(n), because we go through the array once.  
Space: O(n), because the dictionary can store up to every number in the array.
