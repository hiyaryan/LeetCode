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
        This function uses a stack data structure and a hashmap
        to compare closing parenthesis keys with its associated
        matching opening parenthesis values at the top of the
        stack which determines if a set of parenthesis are valid.

        :type s: str
        :rtype: bool
        """
        
        stack = []  # list can represent a stack using stack[-1]
        paren = {')': '(', ']': '[', '}': '{'}
        
        # Loop through all of the parenthesis in the string
        # appending open parenthesis to the stack while comparing
        # the top node with the first closing parenthesis
        for c in s:
            if c in paren:

                # If the stack is not empty and the node at the
                # top of the stack matches the value of the closing
                # parenthesis, the parenthesis is valid.
                if stack and stack[-1] == paren[c]:
                    stack.pop()

                # If the stack is empty or the open parenthesis at 
                # the top of the stack is mismatching then the
                # parenthesis are not valid.
                else:
                    return False

            # If the character is not in the paren dict then it is
            # an open parenthesis, push it on the stack to be the 
            # first up to find its matching closign parenthesis.
            else:
                stack.append(c)

        # If the stack is not empty then not all open parenthesis
        # found a matching closing parenthesis, return False,
        # otherwise, if empty return true.
        return True if not stack else False
    
    
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

