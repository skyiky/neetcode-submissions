class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        ahead_t = 0

        for d, v in sorted(zip(position, speed), reverse=True):
            t = (target - d) / v
            if t > ahead_t:
                fleets += 1
                ahead_t = t
        return fleets