class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hmap = {}
        for n in nums:
            if n in hmap:
                return n
            else:
                hmap[n] = True
        