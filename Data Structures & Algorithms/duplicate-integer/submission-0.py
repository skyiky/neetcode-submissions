class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for n in nums:
            if n in hmap:
                return True
            else:
                hmap[n] = 1
        return False