# Valid Anagram

## Approach
First, check if the two strings have different lengths. If they do, return `False`.  
Use an array of 26 numbers to track the count of each lowercase letter.  
Add to the count for every character in `s`, then subtract for every character in `t`.  
If every count is `0`, both strings contain the same letters and are anagrams.

## Complexity
Time: O(n), because we go through both strings and check the 26-letter array.  
Space: O(1), because the array always contains exactly 26 values.
