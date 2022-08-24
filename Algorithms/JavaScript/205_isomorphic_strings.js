/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {    
    if (s.length !== t.length) {
        return false
    }
    
    let hash = {}
    for (let i = 0; i < s.length; i++) {
        if (hash[s[i]] === undefined) {

            // Ensure value is not already mapped
            let valMapped = false
            Object.values(hash).forEach(val => {
                if (val === t[i]) {
                    valMapped = true
                }
            })

            // If the value is already mapped and not selected using 
            // the existing key, the strings are not isomorphic.
            if (valMapped) {
                return false
            }
            
            hash[s[i]] = t[i]
            
        } else if (hash[s[i]] !== t[i]) {
            return false
        }
    }
    
    return true
}

console.log(true, isIsomorphic("egg", "add"))
console.log(false, isIsomorphic("foo", "bar"))
console.log(true, isIsomorphic("title", "paper"))
console.log(false, isIsomorphic("badc", "bada"))
