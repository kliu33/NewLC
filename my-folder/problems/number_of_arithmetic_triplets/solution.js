/**
 * @param {number[]} nums
 * @param {number} diff
 * @return {number}
 */
var arithmeticTriplets = function(nums, diff) {
    let out = 0;
    for (let num of nums) {
        if (nums.includes(num+diff) && nums.includes(num + ( 2 * diff))){
            out++
        }
    }
    return out;
};