# Encode and Decode Strings

## Approach

Encode each word by placing its length and a `#` before the word.
For example, `"hello"` becomes `"5#hello"`.

To decode, find the next `#` and read the number before it to get the word’s length.
Use that length to extract the complete word, then move to the start of the next encoded word.
Storing the length allows the strings themselves to safely contain `#` characters.

## Complexity

Time: O(n), where `n` is the total number of characters across all strings.
Space: O(n), because the encoded string or decoded list stores all the characters.
