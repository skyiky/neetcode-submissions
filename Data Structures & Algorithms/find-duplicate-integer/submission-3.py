class Solution:
    # A = steps to enter cycle
    # B = steps from cycle entry to meeting point
    # slow traveled T steps
    # fast traveled 2T steps
    # # T = A + B = whole number of cycle laps
    # Starting from the meeting point, which is already B steps past the entry, moving another A steps completes those laps and lands at the entry.
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0 # Starting both at 0 is important because both pointers must follow the same linked path.
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # Phase 2: Find the cycle entry
        # Two arrows entering the same node means two array positions contain that node's number. Therefore, the cycle entry is the duplicate number.
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow

        