# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"


# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Constraints:

#     1 <= strs.length <= 200
#     0 <= strs[i].length <= 200
#     strs[i] consists of only lowercase English letters.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # Prefix has to be shared between all words.
        # Hold the string at index 0 to be matched with 
        # all consecutive strings.
        str0 = strs[0]

        # Compare all strings to strs[0]
        for s in strs[1:]:
            # If the length of either of the two strings to 
            # be compared are larger, take a substring of the
            # word with the length of the smaller string        
            if len(str0) > len(s):
                str0 = str0[0:len(s)]
            else:
                s = s[0:len(str0)]
        
            # Determine the prefix shared between the two strings
            # of the same length.
            while(str0 != s):
                # If all chars have been removed there is no shared
                # prefix, return an empty string.
                if len(str0) == 0 or len(s) == 0:
                    return ""

                # Reduce the size of both strings by a char.
                str0 = str0[0:len(str0) - 1]
                s = s[0:len(s) - 1]

        # The processed strs0 is the prefix shared
        # between all of the strings in the array.
        return str0


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))
print(s.longestCommonPrefix(["preview","pretense","prepend"]))
print(s.longestCommonPrefix(["","b"]))
print(s.longestCommonPrefix(["ab", "a"]))
