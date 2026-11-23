class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Insertion Sort
        for i in range(len(nums)):
            k = i
            while k > 0 and nums[k-1] > nums[k]:
                nums[k-1], nums[k] = nums[k], nums[k-1]
                k -= 1

        return nums