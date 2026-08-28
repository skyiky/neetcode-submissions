from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        candidates = deque()

        for i, x in enumerate(nums):
            while candidates and x > nums[candidates[-1]]:
                candidates.pop()
            candidates.append(i)
            if candidates[0] < i - k + 1:
                candidates.popleft()
            result.append(nums[candidates[0]])

        return result[k-1:]