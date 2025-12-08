from typing import List

# Dogshit
class Solution1:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        return " ".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        return s.split(" ")

class Solution:
    '''
    Encode each string in the result by "length#string"
    '''
    delim = '#'

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        res = ""
        for s in strs:
            res += f"{len(s)}{self.delim}{s}"

        return res


    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            length_digit_list = []
            while s[i] != self.delim:
                length_digit_list.append(s[i])
                i += 1

            length = int(''.join(length_digit_list))
            i += 1 # Iterate over delim

            word = s[i:length+i]
            res.append(word)
            i += length
        
        return res

s = Solution()
i = ["neetasdfjklsajdfklasjdfkljaskldfjaklsdfjaksdfjaskdfjaskdfjasdfkasd","code","love","you"]
i = [""]

encoded = s.encode(i)
print(encoded)

decoded = s.decode(encoded)
print(decoded)
