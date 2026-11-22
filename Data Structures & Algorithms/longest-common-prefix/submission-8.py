class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if not string.startswith(strs[0][0:i+1]):
                    return res
                
            res = strs[0][0:i+1]

        return res