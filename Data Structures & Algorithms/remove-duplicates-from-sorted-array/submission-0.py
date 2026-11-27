class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_seen = None
        pointer = 0

        for i in range(len(nums)):
            curr_num = nums[pointer]
            if last_seen == curr_num:
                nums.pop(pointer)
            else:
                pointer += 1
            
            last_seen = curr_num

        return len(nums)
