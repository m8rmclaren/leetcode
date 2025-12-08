from collections import defaultdict
from typing import List
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We're given a list of numbers and are asked to return the k most frequent elements.
        
        # Let's start by creating a dict storing the frequency of each number.
        
        freq = defaultdict(int) # defaultdict simplifies our future logic
        for num in nums:
            freq[num] += 1

        print(dict(freq))

        # Now, using this dict, we need to create an ordered list of
        # the unique numbers, ordered by their frequency.

        sorted_by_asc = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

        print(sorted_by_asc)

        return list(sorted_by_asc.keys())[0:k]

# TODO another way to solve this is using Bucket Sort.:qa

nums = [1,2,1,2,1,2,3,1,3,2] 
k = 2

s = Solution()
print(s.topKFrequent(nums, k))
