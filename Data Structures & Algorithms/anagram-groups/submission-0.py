class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ordered_strs = ["".join(sorted(x)) for x in strs]
        grouped_dict = {}

        for i, word in enumerate(ordered_strs):
            if word in grouped_dict:
                grouped_dict[word].append(strs[i])
            else:
                grouped_dict[word] = [strs[i]]

        return list(grouped_dict.values())
