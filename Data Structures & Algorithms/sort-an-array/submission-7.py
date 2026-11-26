class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Merge sort
        if len(nums) <= 1:
            return nums

        mid = int(len(nums) / 2)
        l = self.sortArray(nums[:mid])
        r = self.sortArray(nums[mid:])

        return self.merge(l, r)

    def merge(self, l: List[int], r: List[int]):
        new = []
        i = 0
        j = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                new.append(l[i])
                i+=1
            else:
                new.append(r[j])
                j+=1

        new.extend(l[i:])
        new.extend(r[j:])

        return new

