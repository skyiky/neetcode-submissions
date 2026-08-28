class Solution: 
    # answer[i] = product(left side) × product(right side)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            a[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in reversed(range(len(nums))):
            a[i] *= suffix
            suffix *= nums[i]
        
        return a
            
