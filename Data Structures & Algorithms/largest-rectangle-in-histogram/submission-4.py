class Solution:
    # For any fixed contiguous range of bars, the tallest rectangle that fits has height equal to the shortest bar in that range.
    # So the global optimum must:
    # - Have a height equal to at least one bar it spans.
    # - Use that bar as a limiting bar.
    # - Extend as far left and right as possible while all bars remain at least that tall.
    # Key idea: For each bar, assume its height is the rectangle’s limiting height. Find the widest interval containing it where no bar is shorter.
    def largestRectangleArea(self, heights: List[int]) -> int:
        # A (monotonic increasing) stack stores rectangles that are still “open”.
        #    --> Reading from bottom to top, the stored bar heights never decrease.
        stack = [] # (earliest_start, height) 
            # Invariant: stack entry (start, height) means every processed bar from start to the current position is at least height.
        # An active (start, height) entry guarantees no lower bar has appeared since start, because any lower bar would have removed that entry.
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            # When a shorter bar arrives, every taller bar on top can no longer extend right. Therefore, its right boundary is now known, and its area can be calculated.
            while stack and h < stack[-1][1]:
                max_area = max(max_area, stack[-1][1] * (i - stack[-1][0]))
                # The shorter current bar can extend backward through every taller bar that was popped.
                start = stack[-1][0]
                stack.pop()
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area
        
#