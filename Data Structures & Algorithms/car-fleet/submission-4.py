class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        ahead = 0
        for d, v in sorted(zip(position, speed), reverse=True):
            time = (target - d) / v
            if time > ahead:
                fleets += 1
                ahead = time

        return fleets

