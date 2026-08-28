from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for n in strs:
            key = "".join(sorted(n))
            hmap[key].append(n)
        
        result = [values for values in hmap.values()]
        return result