import heapq
class KthLargest:
    # O(N) * (2 * O(logK))
    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k
        for n in nums:
            heapq.heappush(self.h, n) # O(logK)
            if len(self.h) > k:
                heapq.heappop(self.h) # O(logK)

    # O(N) + O(N-1) * O(logN)
    def __init__(self, k: int, nums: List[int]):
        self.h = nums
        self.k = k
        heapq.heapify(self.h) # O(N)
        while len(self.h) > k: # removes N - K elements: worst case k = 1
            heapq.heappop(self.h) # O(logN)

    # O(logK)
    def add(self, val: int) -> int:
        heapq.heappush(self.h, val) # O(logK)
        if len(self.h) > self.k:
            heapq.heappop(self.h) # O(logK)
        return self.h[0]
