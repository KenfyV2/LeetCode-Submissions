class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stored = {}
        
        for word in strs:
            code = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                code[index] += 1
                
            key = tuple(code)

            if key not in stored:
                stored[key] = []
            stored[key].append(word)

        return list(stored.values())

