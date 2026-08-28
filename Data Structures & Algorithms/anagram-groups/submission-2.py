from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for n in strs:
            counts = [0] * 26
            for c in n:
                counts[ord(c) - ord("a")] += 1
            hmap[tuple(counts)].append(n)
        return list(hmap.values())
        # TC: O(NK) where N = len(strs) and K = max string length
        # SC: O(NK)