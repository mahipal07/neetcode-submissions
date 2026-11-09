class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        current_sum = 0
        # Stores frequency of prefix sums encountered so far.
        # Initialized with {0: 1} to handle subarrays starting from index 0.
        prefix_counts = {0: 1}

        for num in nums:
            current_sum += num

            # If (current_sum - k) exists in the map, a subarray summing to k ends here.
            diff = current_sum - k
            if diff in prefix_counts:
                count += prefix_counts[diff]

            # Record/update the current running prefix sum count
            prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

        return count
