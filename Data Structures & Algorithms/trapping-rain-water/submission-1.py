class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l_max, r_max = 0, 0
        l, r = 0, len(height)-1
        
        while l <= r:
            if l_max <= r_max:
                # The branch already chooses the limiting boundary.
                l_max = max(l_max, height[l])
                water += l_max - height[l]
                l += 1
            else:
                r_max = max(r_max, height[r])
                water += r_max - height[r]
                r -= 1

        # For any index:
        # water = min(l_max, r_max) - height[i]
        # This assumes you know the true max on both sides
        
        return water

            


