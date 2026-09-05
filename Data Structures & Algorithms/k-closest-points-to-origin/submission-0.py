import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = [] # min heap
        result = []
        for i, p in enumerate(points): # NlogN
            eucld = math.sqrt(p[0]**2 + p[1]**2)
            heapq.heappush(h, (eucld, i))
        for _ in range(k):
            result.append(points[heapq.heappop(h)[1]]) # KlogN
        return result
        