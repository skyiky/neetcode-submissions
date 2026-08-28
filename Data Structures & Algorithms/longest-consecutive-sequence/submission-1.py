class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        longest = 0

        for num in values:
            if num - 1 not in values:
                size = 1
                num_next = num + 1
                while num_next in values:
                    size += 1
                    num_next += 1
                longest = max(longest, size)

        return longest