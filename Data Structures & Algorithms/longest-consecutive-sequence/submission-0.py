class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for i in nums: 
            if i - 1 not in numset:
                next_idx = 0
                while (i + next_idx) in numset:
                    next_idx += 1
                longest = max(next_idx, longest)
        return longest