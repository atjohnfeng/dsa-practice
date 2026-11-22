class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = self.build_dict(s)
        t_dict = self.build_dict(t)

        return s_dict == t_dict


    def build_dict(self, string: str) -> dict:
        dict = {}
        for letter in string:
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1
        
        return dict
        