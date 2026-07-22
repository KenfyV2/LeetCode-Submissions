# Longest Consecutive Sequence

## Approach

Convert the input array into a set for fast lookups and to remove duplicates.
For each number, check whether `num - 1` is missing from the set. If it is, the number is the beginning of a sequence.

Starting from that number, keep checking the next consecutive numbers until the sequence ends.
Track and return the length of the longest sequence found.

Only starting from the beginning of each sequence prevents us from repeatedly checking the same numbers.

## Complexity

Time: O(n), because each number is processed as part of a consecutive sequence at most once.
Space: O(n), because the set can store every unique number in the input.
