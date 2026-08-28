from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        for n in nums: # create { char -> count } map
            hmap[n] += 1

        bucket = defaultdict(list)
        for n, c in hmap.items(): # create { count -> chars } map
            bucket[c].append(n)
        
        result = []
        for c in range(len(nums), 0, -1): # read in decreasing order of count
            for n in bucket[c]:
                result.append(n)
                if len(result) == k:
                    return result
        # TC: O(N)
        # SC: O(N)