class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,longest,unique = 0,0,set()

        for r,char in enumerate(s):
            while char in unique:
                unique.remove(s[l])
                l += 1
            unique.add(char)
            longest = max(longest,r-l+1)
        return longest