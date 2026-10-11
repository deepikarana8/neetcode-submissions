class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupl = set()
        for i in nums:
            if i in dupl:
                return True
            else:
                dupl.add(i)
        return False