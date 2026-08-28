class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        result = []
        for i in range(len(nums)-2):
            if s[i] > 0:
                break
            
            if i > 0 and s[i] == s[i-1]:
                continue

            l = i+1
            r = len(nums)-1
            while l < r:
                _sum = s[i] + s[l] + s[r]
                if _sum > 0:
                    r -= 1
                elif _sum < 0:
                    l += 1
                else:
                    result.append([s[i], s[l], s[r]])
                    r -= 1
                    l += 1
                    while l < r and s[l] == s[l-1]:
                        l += 1
                    while l < r and s[r] == s[r+1]:
                        r -= 1
        return result

