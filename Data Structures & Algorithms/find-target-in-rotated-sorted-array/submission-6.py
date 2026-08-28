class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. Find the pivot/minimum
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