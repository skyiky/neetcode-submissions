import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []

        for r, v in enumerate(nums):
            heapq.heappush(heap, (-v, r))
            
            while heap[0][1] < r - k + 1:
                heapq.heappop(heap)
            
            result.append(-heap[0][0])
        
        return result[k-1:]

