from typing import List

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # We're given a list of ints height that represents
        # n vertical lines.

        # We can take two numbers in the list & form a 'container'
        # with coordinates (i,0) -> (i, height[i]) and (j,0) -> (j, height[j])

        # Our goal is to determine the maximum area of the container formed by
        # two lines.

        # We can use 2 pointers to find the optimal solution where
        # area = (r-l) * min(height[l], height[r]).
        
        max_area = 0

        l = 0
        r = len(height) - 1

        while l < r:
            area = (r-l) * min(height[l], height[r])

            if area > max_area:
                max_area = area

            # Q: How should I increment/decrement l & r?

            # There must be a relation we can track or property that
            # tells us how to change l & r.

            # Our goal is to *maximize* the size of the tank.
            # If we move the pointer that represents the shorter line,
            # we should end up with the biggest tank.
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return max_area
        

s = Solution()

height = [1,8,6,2,5,4,8,3,7]
print(s.maxArea(height))

