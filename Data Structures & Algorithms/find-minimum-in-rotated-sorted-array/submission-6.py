class Solution:
    # Key Concept: Identify which of the two slices you are in, then where the answer CAN'T be
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]: # list is not rotated
            return nums[0]
        # answer is in the second slice, try to find its beginning (the answer)
        l, r = 0, len(nums)-1
        while l < r:
            mid = (r + l)//2
            if nums[mid] > nums[r]: # mid is part of the first slice still
                l = mid + 1 # because mid cannot be the answer, and the answer MUST be to my right
            elif nums[mid] < nums[r]: # mid is in the second slice now
                r = mid # because mid could be the answer or the answer MUST be to my left
        return nums[l]
