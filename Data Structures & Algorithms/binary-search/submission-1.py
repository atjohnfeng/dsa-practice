class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            middle = low + (high - low) // 2
            middle_value = nums[middle]

            if middle_value == target:
                return middle
            
            if middle_value < target:
                low = middle + 1
            else:
                high = middle - 1
        
        return -1