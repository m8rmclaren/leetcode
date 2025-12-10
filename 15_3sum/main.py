from typing import List

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

class WrongApproachSolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Our problem asks us to return all numbers in the list
        # nums that add up to 0.
        
        # The order of the output & numbers in the output don't matter.

        # We could use the 2 pointer approach to find 3 values
        # by fixing a 3rd pointer in place.

        # Our input array isn't sorted. First we can convert our list
        # to a lookup table. We need to track the value & its index for later
        # verification of the index constraint.
        lookup = {}
        for i in range(len(nums)):
            lookup[nums[i]] = i

        fixed_index = 0

        res = []

        while fixed_index < len(nums):
            fixed = nums[fixed_index]

            for i in range(fixed_index, len(nums)):
                # All indeces must be different
                if i == fixed_index:
                    continue

                # For each iteration, our solution comes in the form:
                # nums[i] + nums[j] = 0 - nums[fixed_index]

                # We can find nums[j] like this:
                # nums[j] = 0 - nums[fixed_index] - nums[i]

                # If (0 - nums[fixed_index] - nums[i]) is in the lookup
                # it's a solution & can be added to the res list

                complete = 0 - fixed - nums[i]
                complete_index = lookup.get(complete)
                if complete in lookup and complete_index != fixed_index and complete_index != i:
                    res.append([fixed, nums[i], complete])
                
            fixed_index += 1

        return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Our problem asks us to return all numbers in the list
        # nums that add up to 0.
        
        # The order of the output & numbers in the output don't matter.

        # We could use the 2 pointer approach to find 3 values
        # by fixing a 3rd pointer in place.

        # Our solution can contain the same input numbers
        # so long as they came from different indices.

        # I think we should sort our input list & use the two pointer
        # approach by fixing one value.
        nums.sort()

        res = []

        for fixed_index in range(len(nums)):

            # We only want to consider the fixed index if it's the first
            # time we've seen that value. IE no duplicates.
            # We could track this in a hash map, but we can also just
            # check directly since nums is sorted.
            if fixed_index > 0 and nums[fixed_index] == nums[fixed_index - 1]:
                continue # Skip this

            # For each iteration, our solution comes in the form:
            # nums[l] + nums[r] + nums[fixed_index] = 0

            l = fixed_index + 1 # Left pointer starts *behind* the fixed index since all prior combos have been tried
            r = len(nums) - 1

            while l < r:
                three_sum = nums[l] + nums[r] + nums[fixed_index]
                # if l == fixed_index:
                #     l += 1
                # if r == fixed_index:
                #     r -= 1

                print(f"l = {l} r = {r}")

                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    res.append([nums[fixed_index], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res

s = Solution()

nums = [-1,0,1,2,-1,-4]
res = s.threeSum(nums)
print(res)

