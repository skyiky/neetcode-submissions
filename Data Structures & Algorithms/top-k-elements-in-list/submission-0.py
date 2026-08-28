from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        for n in nums:
            hmap[n] += 1

        bucket = defaultdict(list)
        for n, c in hmap.items():
            bucket[c].append(n)
        
        result = []
        for c in range(len(nums), 0, -1):
            for n in bucket[c]:
                result.append(n)
                if len(result) == k:
                    return result
        # TC: O(N)
        # SC: O(N)