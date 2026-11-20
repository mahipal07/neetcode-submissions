class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        
        while low <= high:
            mid = low + (high - low) // 2
            res = guess(mid)
            
            if res == 0:
                return mid
            elif res == -1:
                high = mid - 1  # Guess is too high; search the lower half
            else:
                low = mid + 1   # Guess is too low; search the upper half
                
        return -1
