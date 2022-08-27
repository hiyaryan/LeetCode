# Given a string s, find the length of the longest substring without repeating characters.
#
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
#
# Constraints:
#
#     0 <= s.length <= 5 * 104
#     s consists of English letters, digits, symbols and spaces.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Return 0 if the string is empty.
        if len(s) == 0:
        	return 0

        # A dict that keeps track of the chars seen.
        map = {}

        # max_length: keeps track of the max_length of a substring that has
        # 			  no repeating chars.
        #
        # start: keeps track of the starting index of a new substring which
        # 		 is indicated by the first detected repeating char.
        max_length = start = 0

        # For loop should loop through the string by its index which fills
        # the dict with {"char": index}
        for i in range(len(s)):
        	# Check if the char key is in the dict and that the starting
        	# value for the char is less than that in the map.
        	if s[i] in map and start <= map[s[i]]:
        		start = map[s[i]] + 1

        	# Otherwise get the max length by retaining the current value
        	# or of the current substring provided it has a longer length.
        	else:
        		max_length = max(max_length, i - start + 1)

        	# Update the dictionary with {"char": index}
        	map[s[i]] = i
 			

        return max_length



s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))