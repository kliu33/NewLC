/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    let hash_map = {}
    for (let i = 0; i < nums.length; i++){
        if (!hash_map[nums[i]]) hash_map[nums[i]] = [i]
        else {
            if (i - hash_map[nums[i]][hash_map[nums[i]].length -1] <= k) return true
            else {
                hash_map[nums[i]].push(i)
            }
        }
    }
    return false
};