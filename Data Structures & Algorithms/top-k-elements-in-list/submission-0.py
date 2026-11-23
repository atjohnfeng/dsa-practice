class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        sorted_frequencies = sorted(seen.items(), key=lambda item:item[1], reverse=True)

        most_frequent = []
        for i in range(k):
            most_frequent.append(sorted_frequencies[i][0])

        return most_frequent
