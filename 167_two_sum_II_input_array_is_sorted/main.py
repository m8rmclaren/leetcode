from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # n[i] + n[j] = target
        # In a previous problem with an unsorted
        # list on ints, we used a lookup table
        # to solve the prob n[j] = target - n[i]

        # Now we have a sorted list of numbers
        # and we can probably solve it with 2
        # pointers somehow.

        # We're expected to solve the problem in
        # O(n) time.

        # Hint: We can use the two-pointer algorithm. If nums[0] + nums[n-1] > target, 
        # then we know nums[n - 1] can not 
        # possibly be included in any pairs. Why? 
        # Because nums[n - 1] is the largest 
        # element in the array. Even by adding it 
        # with nums[0], which is the smallest 
        # element, we still exceed the target. 
        # You can think of the case when 
        # nums[0] + nums[n - 1] < target.

        # Maybe we brute force it first.

        for i in range(len(numbers)):
            for j in range(len(numbers)):
                
                if i != j and numbers[i] + numbers[j] == target:
                    return [i+1,j+1]

        return [0,0]
