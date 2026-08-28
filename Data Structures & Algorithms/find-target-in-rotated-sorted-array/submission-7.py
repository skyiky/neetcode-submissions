class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Think of the pivot as a boundary between two value groups:
        # indices:  0  1  2  3 | 4  5  6
        # values:  [4, 5, 6, 7 | 0, 1, 2]
        # group:    HIGH       | LOW
        #                        ↑ pivot
        # Compare every value with the final value (2 in this example):
        # value > 2:  True True True True | False False False
        # The pivot is the first False. Binary search finds this boundary.
        # 1. Find the pivot/minimum
        # pivot ∈ [l, r]
        # Every iteration reduces this interval without removing the pivot.
        # Eventually: l == r so that index must be the pivot.
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pivot = l

        # 2. Choose the sorted slice
        if nums[pivot] <= target <= nums[-1]: # target in 2nd slice
            l, r = pivot, len(nums) - 1 
        else: # target in 1st slice
            l, r = 0, pivot - 1

        # 3. Normal binary search
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1