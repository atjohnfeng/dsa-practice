class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        half_length = math.floor(len(s) / 2)
        for i in range(half_length):
            s[i], s[i*-1-1] = s[i*-1-1], s[i]
