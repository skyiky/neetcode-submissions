from collections import deque
class Solution:
    # Key Concept: Remove Candidates That Can Never Win
    # if newer element is larger than the previous, then the previous can NEVER be maximum again
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        candidates = deque() # line of surviving maximum candidates (always decreases left to right)

        for i, x in enumerate(nums):
            while candidates and x > nums[candidates[-1]]:
                candidates.pop() # curr > prev, and prev will leave the current window before curr
            candidates.append(i)
            if candidates[0] < i - k + 1: # remove oldest candidate since outside current window
                candidates.popleft()
            # here, candidates only contains valid (in current window) elements
            if i >= k - 1: # start when i is the last element of the first window
                result.append(nums[candidates[0]]) # head of candidates always contains the max element

        return result