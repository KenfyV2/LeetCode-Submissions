# Group Anagrams

## Approach
Use a dictionary to group words with the same letter counts.  
For each word, create an array of 26 numbers representing how many times each lowercase letter appears.  
Convert the array into a tuple so it can be used as a dictionary key, then add the word to its matching group.  
Return all the groups stored in the dictionary.

## Complexity
Time: O(n × k), where `n` is the number of words and `k` is the average word length.  
Space: O(n × k), because the dictionary stores every word and its anagram group.
