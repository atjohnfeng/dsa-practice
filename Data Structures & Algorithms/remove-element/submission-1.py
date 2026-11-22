class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cleaned = [num for num in nums if num != val]
        k = len(cleaned)
        nums[:k] = cleaned
        return k