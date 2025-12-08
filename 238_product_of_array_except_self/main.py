from typing import List

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

class BruteForceSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # We're given a list of integers, and are asked to
        # return an array of numbers of the same length, where each 
        # index is the *product* of every other element except for
        # the current index in the iteration.

        # One way we could solve this in a brute force way is to use a nested
        # for loop.

        res = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    res[i] *= nums[j]

        return res

class DivisionSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Another way we could solve it is to calculate the product of the whole
        # list & then in a result array divide by the position to
        # "remove that element" from the multiplication.

        n = len(nums)

        product = 1
        for num in nums:
            product = product * num

        for i in range(n):
            nums[i] = int(product / nums[i])

        return nums

# Hint 1: Think how you can efficiently utilize prefix and suffix products to calculate the product of all 
# elements except self for each index. Can you pre-compute the prefix and suffix products in linear 
# time to avoid redundant calculations?

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # The brute force solution is O(n^2). We need to 
        # find a way to store information on each pass so 
        # we don't have to iterate so many times.

        n = len(nums)
        prefix = [1 for _ in range(n)]
        suffix = [1 for _ in range(n)]

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
            suffix[n-1-i] = suffix[n-i] * nums[n-i]

        # Store the result in the given array to use less memory
        for i in range(len(nums)):
            nums[i] = prefix[i] * suffix[i]

        return nums

nums = [1,2,3,4]


s = BruteForceSolution()
s = DivisionSolution()
s = Solution()
print(s.productExceptSelf(nums))
