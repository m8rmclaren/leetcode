from typing import List

# Given n non-negative integers representing an 
# elevation map where the width of each bar is 1, 
# compute how much water it can trap after raining.

class BrainstormSolution:
    def trap(self, height: List[int]) -> int:
        
        # We're given a list of heights representing
        # the height of poles arranged horizontally.
        # The list represents an elevation map.
        
        # Each index is a pole at (i,h)

        # Our goal is to compute the amount of
        # water the poles in the elevation map can hold.

        # This is a tricky question.

        # Q: How should I iterate through the list?

        # The list & its values create a 2D plane.
        # As I'm iterating through, I need to track:
        # 1. Whether the cursor is in water
        # 2. How much water is in the puddle

        # I think we need two steps / parts of the iteration:
        # = One that figures out what the bounds of the puddle are.
        #   E.g., [l, r] with height min(height[l], height[r])
        # = One that figures out how much water is in that section

        # The challenge is that with just a single iteration,
        # we can't know how to track how much water is under the
        # cursor since we don't yet know the depth of the water

        n = len(height)
        l = 0
        r = 0

        lowest_h = 0 # Track the low point of the puddle

        # We scroll along the topo map until there's no more data
        while r < n:

            # 1. Scroll until we find a puddle
            

            # 2. Track the volume (area) the puddle can hold
            
            # 3. Set the left to the end of the last puddle

            pass

        return 0

    def waterInPuddle(self, dim):
        l, r = dim

class BruteForceSolution:
    def trap(self, height: List[int]) -> int:
        
        # We're given a list of heights representing
        # the height of poles arranged horizontally.
        # The list represents an elevation map.
        
        # The simplest way to iterate through
        # the height list is to determine how much
        # water can be held at that specific index.

        # Q: How can I determine how much water can
        # be held at index i?

        # A brute force solution could be to look at every
        # index and figure out if the area above the height is
        # surrounded by either water or land (or air)

        # Hint #2: From the image, we can see that to calculate 
        # the amount of water trapped at a position, the 
        # greater element to the left l and the greater 
        # element to the right r of the current position are 
        # crucial. The formula for the trapped water at 
        # index i is given by: 
        # min(height[l], height[r]) - height[i].

        # Hint #3: A brute force solution would involve iterating 
        # through the array with index i, finding the greater 
        # elements to the left (l) and right (r) for each index, 
        # and then calculating the trapped water for that position. 
        # The total amount of trapped water would be the sum of 
        # the water trapped at each index. Finding l and r for 
        # each index involves repeated work, resulting in an O(n^2) 
        # solution. Can you think of a more efficient approach? 
        # Maybe there is something that we can precompute 
        # and store in arrays.

        # Q: How do I scroll l & r?
        # Q: What do I need to track to help me scroll l & r?

        n = len(height)
        
        capacity = 0
        
        for i in range(n):
            # Brute force solution

            # For each index, find the largest
            # pole to the left and right of i.
            # The amount of water that can be held
            # at i is min(heights[l], heights[r]) - heights[i]

            l = i
            r = i

            # scroll l to the left-most greatest height
            l_max = 0
            while l >= 0:
                if height[l] > l_max:
                    l_max = height[l]
                l -= 1

            # scroll r to the right-most greatest height
            r_max = 0
            while r < n:
                if height[r] > r_max:
                    r_max = height[r]
                r += 1
     
            c = min(l_max, r_max) - height[i]
            print(f'{i}: l_max = {l_max} r_max = {r_max} h = {height[i]} c@i = {c}')
            if c > 0:
                capacity += c

        return capacity

class Solution:
    def trap(self, height: List[int]) -> int:
        
        # We're given a list of heights representing
        # the height of poles arranged horizontally.
        # The list represents an elevation map.

        # A brute force solution is to iterate over each index
        # of the population map & for each index, find
        # the highest peak to the left and right of index i.
        # Then, the amount of water trappable at that index
        # is given by min(height[l], height[l]) - height[i].

        # This is a brute force solution & works in O(n^2).
        
        # Another way we could solve this is to precompute
        # the min/max distances at each index so we can calculate
        # the trapped water in linear time.

        # Alternatively, we can use two-pointer directly
        # to scroll the list of heights, tracking the minimum height
        # of each index.

        n = len(height)
        l = 0
        max_l = height[l]

        r = n - 1
        max_r = height[r]

        res = 0

        # Our l & r pointers scroll independently & will intersect at some point in
        # the middle.
        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                res += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                res += max_r - height[r]
            
        return res
            

s = Solution()

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(s.trap(height))

height = [4,2,0,3,2,5]
print(s.trap(height))

