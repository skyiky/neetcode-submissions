class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        result = set()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                _sum = s[i] + s[l] + s[r]
                if _sum > 0:
                    r -= 1
                elif _sum < 0:
                    l += 1
                else:
                    result.add(tuple([s[i], s[l], s[r]]))
                    r -= 1
                    l += 1
        return [list(_tuple) for _tuple in list(result)]


            


