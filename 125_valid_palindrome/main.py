# A phrase is a palindrome if, after converting all uppercase letters 
# into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters 
# include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

class SuboptimalSolution:
    def isPalindrome(self, s: str) -> bool:

        # This solution requires extra time to clean up the string in the form of a pre-iteration
        # Time: O(2n)
        # Space: O(n)
        
        # Clean up s (lower, strip out all non-alphanumeric chars)
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())

        # We use 2 pointers to scroll through the string
        # and check if the characters are the same.
        # We stop iterating when front == back

        # Q: How do I handle words that don't 
        # have an odd number of characters?

        front = 0
        back = len(s)


        iter = len(s) // 2
        print(f"iter: {iter} len: {len(s)}")

        for _ in range(len(s) // 2):
            print(f"front: {front} ({s[front]}) back: {back} ({s[back-1]})")
            if s[front] != s[back-1]:
                return False

            front += 1
            back -= 1

        return True

class LongSolution:
    def isPalindrome(self, s: str) -> bool:
        # In this solution, I'll try to filter out non-alphanumeric
        # chars in the same iteration loop we use to check if
        # the string is a palindrome

        # I'll do this by using ascii itself.

        # First uppercase char: A -> 65
        # Last uppercase char:  Z -> 90
        
        # First lowercase char: a -> 97  
        # Last lowercase char:  z -> 122

        # To convert from upper to lower, we add (a - A)

        front = 0
        back = len(s)

        offset = ord('a') - ord('A')

        while front < back:
            # print(f"front: {front} ({s[front]}) back: {back} ({s[back-1]})")

            # Convert front & back to lowercase if not already
            f_ascii = ord(s[front])
            if ord('A') <= f_ascii <= ord('Z'):
                f_ascii = f_ascii + offset

            b_ascii = ord(s[back-1])
            if ord('A') <= b_ascii <= ord('Z'):
                b_ascii = b_ascii + offset

            # If the char isn't alphanumeric, skip past it

            is_letter = ord('a') <= f_ascii <= ord('z')
            is_digit = ord('0') <= f_ascii <= ord('9')
            if not (is_letter or is_digit):
                print(f"skip '{s[front]}'")

                front += 1
                continue

            is_letter = ord('a') <= b_ascii <= ord('z')
            is_digit = ord('0') <= b_ascii <= ord('9')
            if not (is_letter or is_digit):
                print(f"skip '{s[back-1]}'")

                back -= 1
                continue

            print(f"front: {front} ({s[front]} -> {chr(f_ascii)}) back: {back} ({s[back-1]} -> {chr(b_ascii)})")
            if f_ascii != b_ascii:
                print("term")
                return False

            front += 1
            back -= 1

        return True

class Solution:
    def isAlphanumeric(self, c: str) -> bool:
        return (ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            # Scroll left ptr right until we get a char
            while l < r and not self.isAlphanumeric(s[l]):
                l += 1

            # Scroll right ptr left until we get a char
            while r > l and not self.isAlphanumeric(s[r]):
                r -= 1
                    
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

sol = Solution()

s = "!A man, a plan, a canal: Panama"
# s = "!race a car"
# s = "9,8"
print(sol.isPalindrome(s))

