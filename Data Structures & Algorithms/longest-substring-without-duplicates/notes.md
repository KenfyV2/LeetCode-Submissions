# Longest Substring Without Repeating Characters

## Approach
Use a sliding window with a set to keep track of unique characters.  
The left pointer `l` marks the start of the window, while the right pointer `r` moves through the string.

If the current character is already in the set, move `l` forward and remove characters until the duplicate is gone.  
Add the current character to the set and calculate the current window length using `r - l + 1`.  
Keep track of the longest valid window found.

## Complexity
Time: O(n), because each character is added and removed from the set at most once.  
Space: O(n), because the set can store up to all unique characters in the string.
