import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-x for x in stones] # max heap
        heapq.heapify(h)

        while len(h) > 1:
            x = -heapq.heappop(h)
            y = -heapq.heappop(h)
            fx = x - y
            if fx > 0:
                heapq.heappush(h, -fx)
        
        return -h[0] if h else 0
