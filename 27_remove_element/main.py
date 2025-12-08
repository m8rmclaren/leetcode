from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums is a list of numbers
        # Our task is to remove each occurance of val from nums
        # and return the number of values *not* equal to val.
        
        # One way to solve this is to shift the whole list down when
        # we encounter val, and fill the end of the array with 0.

        # Another way to solve it is to place val at the end of the array
        # when we encounter it, and replace the index of val with the
        # value at the end of the array.
        
        # The second way is much faster since we don't have to shift down
        # the whole array, where each 'left shift' operation would be O(n).

        # We may run into an edge case, however, where the end of the array
        # is val. In this case, we would be swapping the index of val with val again.
        # There could even be len(nums) occurances of val, in which case there
        # are no numbers & k would be 0.

        # So, we need to have an inner loop that looks at the value at the end of
        # the array & decrements k if it's val.

        # We use 2 pointers, i & k to track our iteration. 
        # i moves 'right' after each iteration, and k moves 'left' as we find occurances of val
        # We want to manipulate i & k independently, so we use a while loop

        i = 0
        k = len(nums)
        while i < k:
            if nums[i] == val:
                nums[i] = nums[k-1]
                print(f"replace nums[{i}] with nums[{k-1}]")
                k -= 1
            else:
                print(f"nums[{i}] != val")
                i += 1

        return k

def run(nums, val):
    s = Solution()
    print(f"input:\nnums:{nums}\nval:{val}")

    k = s.removeElement(nums, val)
    print(f"\noutput:\nnums:{nums}\nk:{k}")

# nums = [3,2,2,3]
# val = 3
# run(nums, val)

nums = [0,1,2,2,3,0,4,2]
val = 2
run(nums, val)
