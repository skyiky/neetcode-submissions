class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}
        for n in s:
            if n in hmap:
                hmap[n] = hmap[n] + 1
            else:
                hmap[n] = 1
        for n in t:
            if n in hmap:
                hmap[n] = hmap[n] - 1
                if hmap[n] < 0:
                    return False
            else:
                return False
        for key, val in hmap.items():
            if val != 0:
                return False
        return True