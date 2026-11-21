import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2
            hours = 0
            
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                res = k
                right = k - 1  # Try to find a smaller valid eating speed
            else:
                left = k + 1   # Eating speed is too slow, increase it

        return res
import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2
            hours = 0
            
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                res = k
                right = k - 1  # Try to find a smaller valid eating speed
            else:
                left = k + 1   # Eating speed is too slow, increase it

        return res
 
        