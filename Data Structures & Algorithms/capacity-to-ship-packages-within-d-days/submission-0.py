class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = left + (right - left) // 2
            days_needed = 1
            current_load = 0
            
            for w in weights:
                if current_load + w > mid:
                    days_needed += 1
                    current_load = 0
                current_load += w
                
            if days_needed <= days:
                right = mid
            else:
                left = mid + 1
                
        return left
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = left + (right - left) // 2
            days_needed = 1
            current_load = 0
            
            for w in weights:
                if current_load + w > mid:
                    days_needed += 1
                    current_load = 0
                current_load += w
                
            if days_needed <= days:
                right = mid
            else:
                left = mid + 1
                
        return left
 
        