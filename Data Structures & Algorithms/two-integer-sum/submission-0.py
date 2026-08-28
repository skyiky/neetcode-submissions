class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {} # { value: index }
        for i in range(len(nums)):
            c_val = target - nums[i]
            if c_val in hmap:
                return [hmap[c_val], i]
            else:
                hmap[nums[i]] = i
        return []