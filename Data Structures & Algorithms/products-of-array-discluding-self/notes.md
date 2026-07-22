# Product of Array Except Self

## Approach
Use the result array to store the product of all numbers before each index.  
Move from left to right while keeping a running prefix product.

Then move from right to left while keeping a running postfix product.  
Multiply each value in the result array by its postfix product.

This gives the product of every number except the number at the current index without using division.

## Complexity
Time: O(n), because we go through the array twice.  
Space: O(1) extra space, because only `pre` and `post` are used outside the output array.
