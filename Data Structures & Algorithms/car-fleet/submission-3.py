class Solution:
    # Compare arrival times:
    #   Behind arrives earlier or equal: it must catch the fleet ahead.
    #   Behind arrives later: it cannot catch the fleet ahead.
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        ahead_t = 0
        # sort and iterate starting from the car closest to the target
        # if the car catches the car ahead of it, it joins its fleet
        for d, v in sorted(zip(position, speed), reverse=True):
            t = (target - d) / v
            if t > ahead_t:
                fleets += 1
                ahead_t = t
        return fleets