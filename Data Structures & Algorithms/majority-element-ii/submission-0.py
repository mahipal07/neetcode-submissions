class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        # Step 1: Find candidate elements
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verify candidates
        result = []
        threshold = len(nums) // 3
        for candidate in (candidate1, candidate2):
            if candidate is not None and nums.count(candidate) > threshold:
                result.append(candidate)

        return result
