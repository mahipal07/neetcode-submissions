from collections import Counter
from typing import List


class Solution:

  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = Counter(nums)

    # Buckets where index represents frequency (0 to len(nums))
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
      buckets[freq].append(num)

    # Collect numbers starting from the highest frequency
    res = []
    for freq in range(len(buckets) - 1, 0, -1):
      for num in buckets[freq]:
        res.append(num)
        if len(res) == k:
          return res
from collections import Counter
from typing import List


class Solution:

  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = Counter(nums)

    # Buckets where index represents frequency (0 to len(nums))
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
      buckets[freq].append(num)

    # Collect numbers starting from the highest frequency
    res = []
    for freq in range(len(buckets) - 1, 0, -1):
      for num in buckets[freq]:
        res.append(num)
        if len(res) == k:
          return res
 
        