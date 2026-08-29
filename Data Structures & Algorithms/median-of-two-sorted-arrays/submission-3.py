class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        half = (len(nums1) + len(nums2) + 1)//2
        
        l, r = 0, len(nums1)
        while l <= r:
            i = (l + r)//2
            j = half - i 

            left1 = nums1[i-1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < len(nums1) else float('inf')
            left2 = nums2[j-1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < len(nums2) else float('inf')
            
            if left1 <= right2 and left2 <= right1:
                if (len(nums1) + len(nums2))%2:
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2))/2
            
            if left1 > right2:
                r = i - 1
            else:
                l = i + 1



            

