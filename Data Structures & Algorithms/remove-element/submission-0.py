class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cleaned = [num for num in nums if num != val]
        nums[:len(cleaned)] = cleaned
        return len(cleaned)