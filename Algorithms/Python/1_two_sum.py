# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]


# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# Constraints:

#     2 <= nums.length <= 104
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109
#     Only one valid answer exists.
 
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

class Solution(object):
    # twoSum is O(n^2)
    def twoSum2(self, nums, target):
        for i, n in enumerate(nums):
            for j, m in enumerate(nums[i + 1:]):      
                if n + m == target:
                    return [i, j + i + 1]

    # twoSum2 less than O(n)
    def twoSum(self, nums, target):
        # 1. answer = [], return // stores two idices of integers that add to the target
        # 2. while-loop while length(nums) > 0 over all nums from nums[-1:] 
        # 3. If the sum of any of those elements equals the target then return answer
        # 4. Otherwise: pop() the element
        # 5. Check the next nums[-1:]--

        i = len(nums) - 2
        while (True):
            if nums[i] + nums[-1] == target:
                return [i, len(nums) - 1]

            else:
                nums.pop()
                i = i - 1
        
      

s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 6))
print(s.twoSum([3,3], 6))


# print(s.twoSum2([2,7,11,15], 9))
# print(s.twoSum2([3,2,4], 6))
# print(s.twoSum2([3,3], 6))
