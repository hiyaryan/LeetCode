# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
#     For example, 121 is a palindrome while 123 is not.


# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.


# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 
# Constraints:
#     -231 <= x <= 231 - 1

# Follow up: Could you solve it without converting the integer to a string?

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # Negative numbers are not palindromes
        if (x < 0):
            return False

        # Convert x to a string then reverse it
        y = str(x)[::-1]

        # If y typcasted to an int is equal to x then it is a palindrome
        if int(y) == x:
            return True

        # If the test above fails the the number is not a palindrome.
        return False

        
# Tests
s = Solution()
print(f'121 is a palindrome? {s.isPalindrome(121)}')
print(f'-121 is a palindrome? {s.isPalindrome(-121)}')
print(f'10 is a palindrome? {s.isPalindrome(10)}')
    
