from typing import List

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # First, let's build a dict mapping each str to a dict of the frequency each 
        # letter occurs in it.
        counts = {}

        for s in strs:
            count = {}
            for c in s:
                count[c] = 1 + count.get(c, 0) # Init val to 0 if key not in count
            
            counts[s] = count
        
        print(counts)
        
        # Now, we need to group the elements of counts that are equal element-wise
        # Said differently, we want to group all the identical count dicts together

        res = {}
        for w, c in counts.items():
            res[c] = res.get(c, []) + w

        print(res)
            

        return [[""]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Our goal in this problem is to group related elements together.
        #
        # At first, I wanted to determine if strings were anagrams by
        # counting the frequency of each letter, storing in a dict, & comparing the
        # dicts to each other. 
        # The issue with this approach is that at my current skill level, the 
        # only way I know how to group elements together is using a dict, and I can't
        # index a dict with a dict.
        #
        # Instead, I'll first sort each string in strs in an intermediate data structure..

        # For this solution,
        # Time complexity: O(m * nlog(n)) where m = len(strs) & n is the 
        #                  average length of a string. sort works in nlog(n) time.
        # Space complexity: O(m) since we're creating a duplicate sized structure to hold res.

        res = {}
        for s in strs:
            s_list = list(s)
            s_list.sort()

            s_sorted_str = "".join(s_list)

            an = res.setdefault(s_sorted_str, [])
            an.append(s)

        return list(res.values())

strs = ["eat","tea","tan","ate","nat","bat"]
expected_output = [["bat"],["nat","tan"],["ate","eat","tea"]]

s = Solution()

print(s.groupAnagrams(strs))
