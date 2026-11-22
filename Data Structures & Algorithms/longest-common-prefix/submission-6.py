class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        first_word = strs[0]

        for i in range(len(first_word)):
            prefix = first_word[0:i+1]
            for string in strs:
                if not string.startswith(prefix):
                    return prefix[0:i]

        return first_word
