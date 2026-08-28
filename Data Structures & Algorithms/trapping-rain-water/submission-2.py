class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        lmax = 0
        rmax = 0

        l = 0
        r = len(height) - 1
        while l <= r:
            if lmax <= rmax:
                lmax = max(lmax, height[l])
                water += lmax - height[l]
                l += 1
            else:
                rmax = max(rmax, height[r])
                water += rmax - height[r]
                r -= 1

        return water

