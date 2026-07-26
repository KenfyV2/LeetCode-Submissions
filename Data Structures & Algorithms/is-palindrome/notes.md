# Valid Palindrome

## Approach
Use two pointers, one starting at the beginning and one at the end of the string.  
Move each pointer past any character that is not a letter or number.  
Compare the valid characters after converting them to lowercase.

If the characters do not match, return `False`.  
Continue moving the pointers toward the center, and return `True` if every pair matches.

## Complexity
Time: O(n), because each character is checked at most once.  
Space: O(1), because only two pointers are used.
