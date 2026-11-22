class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            
            # If mid element is greater than the right element, 
            # the minimum must be to the right of mid.
            if nums[mid] > nums[r]:
                l = mid + 1
            # Otherwise, the minimum is at mid or to the left of mid.
            else:
                r = mid
                
        return nums[l]
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            
            # If mid element is greater than the right element, 
            # the minimum must be to the right of mid.
            if nums[mid] > nums[r]:
                l = mid + 1
            # Otherwise, the minimum is at mid or to the left of mid.
            else:
                r = mid
                
        return nums[l]
 
        