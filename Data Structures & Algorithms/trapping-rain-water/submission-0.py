class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        l_max, r_max = 0, 0
        l, r = 0, len(height)-1
        
        while l <= r:
            if l_max <= r_max:
                l_max = max(l_max, height[l])
                result += max(min(l_max, r_max) - height[l], 0)
                l += 1
            else:
                r_max = max(r_max, height[r])
                result += max(min(l_max, r_max) - height[r], 0)
                r -= 1
        
        return result

            


