class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        x = 1
        for n in nums:
            if n == 0:
                zeros += 1
            else:
                x *= n
        
        result = [x] * len(nums)
        if zeros > 1:
            return [0] * len(nums)
        elif zeros == 1:
            result = [0] * len(nums)
        
        for i, v in enumerate(nums):
            if v == 0:
                result[i] = x
            else:
                result[i] //= v
        return result