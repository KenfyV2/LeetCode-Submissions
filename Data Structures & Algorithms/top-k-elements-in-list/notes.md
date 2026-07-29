# Top K Frequent Elements

## Approach 1: Sorting

Use a dictionary to count how many times each number appears.
Sort the unique numbers by their frequency from highest to lowest.
Return the first `k` numbers from the sorted list.

### Complexity

Time: O(n + m log m), where `n` is the length of the input and `m` is the number of unique numbers.
Space: O(m), because the dictionary and sorted list store the unique numbers.

## Approach 2: Bucket Sort

Use a dictionary to count how many times each number appears.
Create a bucket array where each index represents a frequency.
Place each number into the bucket that matches its frequency.

Go through the buckets from the highest frequency to the lowest and add numbers to the result.
Return the result once it contains `k` numbers.

Bucket sort is faster because it avoids sorting all the unique numbers.

### Complexity

Time: O(n), because we count the numbers, fill the buckets, and scan through them once.
Space: O(n), because the dictionary and buckets can store up to every number in the input.
