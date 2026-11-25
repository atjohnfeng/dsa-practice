class Solution:
    def binary_search_recursion(self, nums: List[int], target: int, l_index: int, r_index: int) -> int:
        if l_index > r_index:
            return -1

        m_index = l_index + (r_index - l_index) // 2
        middle_value = nums[m_index]

        if middle_value == target:
            return m_index

        if middle_value > target:
            return self.binary_search_recursion(nums, target, l_index, m_index - 1)
        else:
            return self.binary_search_recursion(nums, target, m_index + 1, r_index)


    def search(self, nums: List[int], target:int):
        return self.binary_search_recursion(nums, target, 0, len(nums)-1)
