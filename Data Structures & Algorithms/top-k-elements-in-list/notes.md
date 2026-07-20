# Top K Frequent Elements

## Approach
Use a dictionary to count how many times each number appears.  
Sort the unique numbers by their frequency from highest to lowest.  
Return the first `k` numbers from the sorted list.

A bucket sort solution is faster because frequencies can only range from `1` to `n`.  
Using buckets can reduce the time complexity to O(n).

## Complexity
Time: O(n + m log m), where `n` is the length of the input and `m` is the number of unique numbers.  
Space: O(m), because the dictionary and sorted list store the unique numbers.

## Faster Approach
Bucket sort can solve this problem in O(n) time and O(n) space.
