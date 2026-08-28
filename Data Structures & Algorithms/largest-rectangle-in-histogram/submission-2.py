class Solution:
    # For any fixed contiguous range of bars, the tallest rectangle that fits has height equal to the shortest bar in that range.
    # So the global optimum must:
    # - Have a height equal to at least one bar it spans.
    # - Use that bar as a limiting bar.
    # - Extend as far left and right as possible while all bars remain at least that tall.
    # Key idea: For each bar, assume its height is the rectangle’s limiting height. Find the widest interval containing it where no bar is shorter.
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (earliest_start, height)
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                max_area = max(max_area, stack[-1][1] * (i - stack[-1][0]))
                start = stack[-1][0]
                stack.pop()
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area
        