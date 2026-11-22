class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_num = math.ceil(len(nums) / 2)

        seen = {}

        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

            if seen[num] == majority_num:
                    return num
