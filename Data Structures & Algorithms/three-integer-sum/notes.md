# 3Sum

## Approach

Sort the array so we can use two pointers.
Loop through each number and treat it as the first number in the triplet.

For each first number, place a left pointer after it and a right pointer at the end of the array.
If the sum is too small, move the left pointer right.
If the sum is too large, move the right pointer left.
If the sum is `0`, add the triplet to the result.

Skip duplicate first numbers and duplicate left-pointer values to avoid returning the same triplet more than once.

## Complexity

Time: O(n²), because sorting takes O(n log n), and the two-pointer search takes O(n²).
Space: O(1) extra space, not including the output list. Python’s sorting may use additional space internally.
