import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return heapq.nlargest(k, nums)[-1]

        h = [] # min heap of size k
        for n in nums:
            if len(h) < k:
                heapq.heappush(h, n)
            elif n > h[0]:
                heapq.heapreplace(h, n)
        return h[0]