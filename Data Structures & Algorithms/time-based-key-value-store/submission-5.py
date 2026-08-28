from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hmap[key]
        l, r = 0, len(arr)-1
        ans = ""
        while l <= r: # a valid answer is not guaranteed --> need to examine the final element
            m = (r+l)//2 # when l==r this means either 1. length one 2. last element
            if arr[m][0] == timestamp: # early return
                return arr[m][1]
            if arr[m][0] > timestamp:
                r = m - 1
            else:
                ans = arr[m][1]
                l = m + 1
        return ans


        
