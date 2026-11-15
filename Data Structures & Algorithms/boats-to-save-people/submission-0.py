class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
        
        while left <= right:
            # If the lightest and heaviest person can share a boat, pair them
            if people[left] + people[right] <= limit:
                left += 1
            
            # The heaviest person always gets on a boat (either paired or alone)
            right -= 1
            boats += 1
            
        return boats
