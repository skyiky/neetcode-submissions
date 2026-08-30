class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0 #Starting both at 0 is important because both pointers must follow the same linked path.
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # Phase 2: Find the cycle entry.
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow

        