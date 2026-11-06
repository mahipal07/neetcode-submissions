class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def max_heapify(n: int, i: int) -> None:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and nums[left] > nums[largest]:
                largest = left

            if right < n and nums[right] > nums[largest]:
                largest = right

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                max_heapify(n, largest)

        n = len(nums)

        # Build max heap (from the last non-leaf node up to root)
        for i in range(n // 2 - 1, -1, -1):
            max_heapify(n, i)

        # Extract elements one by one from the heap
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]  # Move current root to the end
            max_heapify(i, 0)                   # Call heapify on the reduced heap

        return nums
