class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        current_longest_prefix = ""
        ending_index = 0
        first_word = strs[0]

        while ending_index <= len(first_word):
            curr_prefix = first_word[0:ending_index]

            for word in strs:
                if curr_prefix not in word and curr_prefix != "":
                    return current_longest_prefix
            ending_index += 1
            current_longest_prefix = curr_prefix

        return current_longest_prefix
