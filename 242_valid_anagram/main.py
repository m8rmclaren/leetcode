class Solution:
    def getFreq(self, s: str):
        letter_freq = {}

        for l in s:
            letter_freq[l] = 1 + letter_freq.get(l, 0) # get takes default param

        return letter_freq

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Space complexity: O(s+t)
        # Time complexity: O(s+t)
        letter_freq_in_s = self.getFreq(s)
        letter_freq_in_t = self.getFreq(t)

        return letter_freq_in_s == letter_freq_in_t

# One iteration instead of 2
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Space complexity: O(s+t)
        # Time complexity: O(s)
        letter_freq_in_s = {}
        letter_freq_in_t = {}

        for i in range(len(s)):
            letter_freq_in_s[s[i]] = 1 + letter_freq_in_s.get(s[i], 0) # get takes default param
            letter_freq_in_t[t[i]] = 1 + letter_freq_in_t.get(t[i], 0)

        return letter_freq_in_s == letter_freq_in_t

class Solution2:
    # Less time & space efficient?
    def isAnagram(self, s: str, t: str) -> bool:
        sList = list(s)
        tList = list(t)

        sList.sort()
        tList.sort()

        return sList == tList


s = "anagram"
t = "nagaram"
