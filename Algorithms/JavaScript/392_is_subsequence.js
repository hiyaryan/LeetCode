// Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

// A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

// Example 1:

// Input: s = "abc", t = "ahbgdc"
// Output: true

// Example 2:

// Input: s = "axc", t = "ahbgdc"
// Output: false

 

// Constraints:

//     0 <= s.length <= 100
//     0 <= t.length <= 104
//     s and t consist only of lowercase English letters.

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let inSequence = false
    s = s.split("")
    for (let i = 0; i < t.length; i++) {
        console.log(s)

        if (s[0] === t[i]) {
            s.shift()
        }
    }

    if (s.length === 0) {
        console.log(s)
        inSequence = true
    }
    
    return inSequence  
};

console.log(isSubsequence("abc", "ahbgdc"))
console.log(isSubsequence("axc", "ahbgdc"))
console.log(isSubsequence("a", "a"))
console.log(isSubsequence("b", "a"))

