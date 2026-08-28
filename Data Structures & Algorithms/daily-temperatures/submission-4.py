# The key phrase is “the nearest future day with a greater value”: this is the Next Greater Element pattern, which suggests a monotonic stack.
class Solution:
    # There are two optimal approaches:
    # Forward scan: stack holds past days still waiting for a warmer day; the current temperature resolves them.
    # Reverse scan: stack holds useful future-day candidates; smaller/equal candidates are removed.
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev
            stack.append(i)
        return result
            
            
                