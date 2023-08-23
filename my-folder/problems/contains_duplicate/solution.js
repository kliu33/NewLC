/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let s1 = new Set();
    for (let num of nums){
        if (s1.has(num)) return true
        s1.add(num)
    }
    return false
};