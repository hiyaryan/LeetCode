// Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

// A subarray is a contiguous part of an array.



// Example 1:

// Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
// Output: 6
// Explanation: [4,-1,2,1] has the largest sum = 6.

// Example 2:

// Input: nums = [1]
// Output: 1

// Example 3:

// Input: nums = [5,4,-1,7,8]
// Output: 23



// Constraints:

//     1 <= nums.length <= 105
//     -104 <= nums[i] <= 104

/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let pivot = 0
    let lhs = 0
    let rhs = 0
    while (pivot !== nums.length) {

        for (let i = 0; i < pivot; i++) {
            lhs += nums[i]
        }

        for (let j = nums.length - 1; j > pivot; j--) {
            rhs += nums[j]
        }

        if (rhs === lhs) {
            // console.log(lhs, rhs)

            return pivot
        }

        rhs = 0
        lhs = 0
        pivot++
    }

    return -1
};

// output: 3
console.log(pivotIndex([1, 7, 3, 6, 5, 6]))
console.log(pivotIndex([1, 2, 3]))
console.log(pivotIndex([2, 1, -1]))
