class Solution:
    # For any fixed contiguous range of bars, the tallest rectangle that fits has height equal to the shortest bar in that range.
    # So the global optimum must:
    # - Have a height equal to at least one bar it spans.
    # - Use that bar as a limiting bar.
    # - Extend as far left and right as possible while all bars remain at least that tall.
    # Key idea: For each bar, assume its height is the rectangle’s limiting height. Find the widest interval containing it where no bar is shorter.
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        rbi = [size-1] * size
        lbi = [0] * size
        stack = [] # holds elements where right boundary is not determined
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                rbi[stack[-1]] = i - 1
                stack.pop()
            stack.append(i)
        
        stack = []
        for i, h in reversed(list(enumerate(heights))):
            while stack and h < heights[stack[-1]]:
                lbi[stack[-1]] = i + 1
                stack.pop()
            stack.append(i)
        
        _max = 0
        for i in range(size):
            _max = max(_max, heights[i] * (rbi[i] - lbi[i] + 1))

        return _max


        