# Container With Most Water

## Approach
Use two pointers, one at the beginning and one at the end of the array.  
Calculate the area using the distance between the pointers as the width and the shorter height as the container height.

Keep track of the maximum area found.  
Move the pointer with the shorter height inward, because keeping the shorter height cannot produce a larger area as the width gets smaller.

Continue until the two pointers meet.

## Complexity
Time: O(n), because each pointer moves through the array at most once.  
Space: O(1), because only a few variables and two pointers are used.
