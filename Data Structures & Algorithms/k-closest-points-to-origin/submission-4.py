import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # O(NlogK)
        # return heapq.nsmallest(k, points, lambda p: math.sqrt(p[0]**2 + p[1]**2))

        # O(NlogK)
        # nsmallest implementation:
        h = [] # max heap constrained to size k
        for p in points:
            d = p[0] ** 2 + p[1] ** 2 # optimize away math.sqrt
            if len(h) < k: # fill up the heap until k
                heapq.heappush(h, (-d, p))
            elif d < -h[0][0]:
                heapq.heapreplace(h, (-d, p))
        return [p for _, p in h]
            