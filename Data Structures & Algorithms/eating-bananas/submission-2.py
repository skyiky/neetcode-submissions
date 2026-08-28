class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r: # When l and r become equal, only one candidate remains
            spd = (r + l)//2
            time = sum(
                (p + spd - 1)//spd # math trick to calculate ceiling
                for p in piles
            )
            if time <= h:
                r = spd # fast enough, but maybe better answer exists, so keep it as top boundary
            else:
                l = spd + 1 # too slow, spd cannot be valid ans, so omit it.
        return l # only one candidate, return either l or r since l == r
        
                
