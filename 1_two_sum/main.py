from typing import List

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Brute force solution. Use 2 pointers
        # Time complexity: O(n^2)
        # Space complexity: O(1)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
        
        # We won't ever get here since there's always an answer, 
        # but we return a value for completeness
        return [0,0]

# Better solution
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Create a lookup table from the number to its index in the nums array
        lookup_table = {}
        for i in range(len(nums)):
            lookup_table[nums[i]] = i
        
        # Our formula to find the sum is target = i + j
        # If we fix i, our formula becomes target - i = j
        # 
        # If j exists in the lookup table, we return [i, lookup_table[target - i]]

        for i in range(len(nums)):
            j = target - nums[i]

            if lookup_table.get(j) is not None and i != lookup_table.get(j):
                return [i, lookup_table[j]]

        return [0,0]
