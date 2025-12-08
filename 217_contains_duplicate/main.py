from typing import List

class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = {}

        for num in nums:
            if table.get(num) is None:
                table[num] = 1
            else:
                table[num] += 1

            if table[num] > 1:
                return True
        
        return False

# This solution is better than Solution1 because we don't track the unnecessary data point of
# how often a number occurs; we just track if it does occur. IE, the problem statement doesn't ask "how many times
# does a value occur", just if a value occurs more than once.
#
# To spell it out, it has less conditional logic which costs time, and it occupies less space for unnecessary data.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = set()

        for num in nums:
            if num in table:
                return True

            table.add(num)
        
        return False
