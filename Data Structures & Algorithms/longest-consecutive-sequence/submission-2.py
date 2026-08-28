class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        longest = 0

        # num is a value, not an array position.
        # This loop means: "Inspect every number once"
        for num in values: # Job 1: find sequence starts
            if num - 1 not in values:
                size = 1
                num_next = num + 1 
                while num_next in values: # Job 2: extend the sequence
                    size += 1             # Membership checking creates a virtual number line
                    num_next += 1
                longest = max(longest, size)

        return longest