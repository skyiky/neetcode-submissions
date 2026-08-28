class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        result = 0
        for n in s:
            if n-1 not in s:
                size = 1
                n_next = n+1
                while n_next in s:
                    size += 1
                    n_next += 1
                result = max(result, size)
        return result