# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
#   1. Open brackets must be closed by the same type of brackets.
#   2. Open brackets must be closed in the correct order.
#   3. Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 1:
#
# Input: s = "()"
# Output: true
#
#
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
#
#
# Example 3:
#
# Input: s = "(]"
# Output: false
#
#
# Constraints:
#
#    1 <= s.length <= 104
#    s consists of parentheses only '()[]{}'.



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if len(s) % 2 == 1:
            return False
        
        paren = {
            '(': False,
            ')': False,
            '[': False,
            ']': False,
            '{': False,
            '}': False,
        }
        
        return paren
    
    
    def isValidNotNested(self, s):
        """
        This function only works if parenthesis are not nested.
            
        :type s: str
        :rtype: bool
        """
        
        # A valid set of parenthesis always come in pairs, therefore,
        # if the length of the list is an odd number it is invalid.
        if len(s) % 2 == 1:
            return False
        
        # ASCII values for opening and closing parenthesis are near
        # in value, therefore if the difference between them is larger
        # than, say 5, then the parenthesis are not valid
        for i, p in enumerate(s[1:]):
            
            # If the ASCII value is less than 5 than the parenthesis are valid.
            if ord(p) - ord(s[i]) < 5:
                i = i + 1
            
            # If i is an odd int then the closing parenthesis is being compared to
            # the opening parenthesis of the next set therefore do nothing.
            elif i % 2 == 1:
                pass
            
            # The parenthesis are not valid.
            else:
                return False
    
        # The for loop runs the validity test, if it finishes then the
        # parenthesis are valid.
        return True


s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))

print(s.isValid("{[]}"))
print(s.isValid("("))
print(s.isValid("()["))


