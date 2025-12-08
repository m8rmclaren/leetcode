import sys
from typing import List

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Hint 1:
# Is there any way to identify the start of a sequence? 
# For example, in [1, 2, 3, 10, 11, 12], only 1 and 10 
# are the beginning of a sequence. Instead of trying to 
# form a sequence for every number, we should 
# only consider numbers like 1 and 10.

# Hint 2:
# We can consider a number num as the start of a sequence 
# if and only if num - 1 does not exist in the given array.
# We iterate through the array and only start building the 
# sequence if it is the start of a sequence. This avoids 
# repeated work. We can use a hash set for O(1) lookups 
# by converting the array to a hash set.

class BruteForceSolution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # We're given an unsorted list of numbers.
        # We're asked to return the length of the longest consecutive
        # elements in the list & we must do it in O(n) time.

        # A consecutive sequence is a sequence of elements in which each element 
        # is exactly 1 greater than the previous element. The elements 
        # do not have to be consecutive in the original array.

        # If we were allowed to use any time complexity, we could
        # sort the list & then use 2 pointers to find the length
        # of the longest run.

        # However, the O(n) time constraint only allows us to iterate over
        # the list one time.

        # My confusion is coming from the list being unsorted.
        # How do we find consecutive elements if the element we're looking
        # at came before the element we're currently looking at?

        # Hint 2 tells us we can consider an element as the start of a sequence
        # if num-1 is not present in the list of numbers.

        # First, brute force solution

        lookup = set(nums)

        longest = 0
        for i in range(len(nums)):
            current_sequence = 1
            num = nums[i]

            while True:
                if num+1 in lookup:
                    num += 1
                    current_sequence += 1
                else:
                    if current_sequence > longest:
                        longest = current_sequence
                    break

        return longest

nums = [100,4,200,1,3,2]
# nums = [0,3,7,2,5,8,4,6,0,1]

s = BruteForceSolution()

seq_len = s.longestConsecutive([100,4,200,1,3,2])
if seq_len != 4:
    sys.exit(1)

seq_len = s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
if seq_len != 9:
    sys.exit(1)

seq_len = s.longestConsecutive([1,0,1,2])
if seq_len != 3:
    sys.exit(1)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # We're given an unsorted list of numbers.
        # We're asked to return the length of the longest consecutive
        # elements in the list & we must do it in O(n) time.

        # A consecutive sequence is a sequence of elements in which each element 
        # is exactly 1 greater than the previous element. The elements 
        # do not have to be consecutive in the original array.

        # The brute force solution is to consider every element as the beginning
        # of a sequence.

        # This isn't great.
        # Hint 2 tells us we can consider an element as the start of a sequence
        # if num-1 is not present in the list of numbers.

        # So, what we can do first is build a list containing the first number
        # of every sequence in the list.

        lookup = set(nums)

        starting_sequences = set()
        for num in nums:
            if num-1 not in lookup:
                starting_sequences.add(num)
        
        print(starting_sequences)

        # Now, we can just look at each of the starting sequence and
        # figure out which one is the longest
        longest = 0

        for cur in starting_sequences:
            current_sequence = 1
            while True:
                if cur+1 in lookup:
                    cur += 1
                    current_sequence += 1
                else:
                    if current_sequence > longest:
                        longest = current_sequence
                    break
        
        return longest

s = Solution()

seq_len = s.longestConsecutive([100,4,200,1,3,2])
if seq_len != 4:
    sys.exit(1)

seq_len = s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
if seq_len != 9:
    sys.exit(1)

seq_len = s.longestConsecutive([1,0,1,2])
if seq_len != 3:
    sys.exit(1)
