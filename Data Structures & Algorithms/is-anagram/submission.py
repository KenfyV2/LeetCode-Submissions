class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        code = [0] * 26
        for char in s:
            index = ord(char) - ord('a')
            code[index] += 1

        for char in t:
            index = ord(char) - ord('a')
            code[index] -= 1

        for num in code:
            if 0 != num:
                return False
        return True
