import heapq
class Solution:
    # Keep the worst retained element at the root so better candidates can replace it: 
    # a min-heap for the K largest, or a max-heap for the K smallest.
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return heapq.nlargest(k, nums)[-1]

        h = [] # min heap of size k
        for n in nums:
            if len(h) < k:
                heapq.heappush(h, n)
            elif n > h[0]:
                heapq.heapreplace(h, n)
        return h[0]