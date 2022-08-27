# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# 
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
# Example 1:
#
# Input: nums = [1,1,1], k = 2
# Output: 2
#
#
# Example 2:
#
# Input: nums = [1,2,3], k = 3
# Output: 2
#
#
# Constraints:
#
#     1 <= nums.length <= 2 * 104
#     -1000 <= nums[i] <= 1000
#     -107 <= k <= 107


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumdict = {0:1}
        n = len(nums)
        
        count = 0
        s = 0

        for num in nums:
        	s += num

        	if s-k in sumdict:
        		count += sumdict[s-k]

        	if s in sumdict:
        		sumdict[s] += 1

        	else:
        		sumdict[s] = 1

        return count


s = Solution()
print(s.subarraySum([1,1,1], 2))
print(s.subarraySum([1,2,3], 3))