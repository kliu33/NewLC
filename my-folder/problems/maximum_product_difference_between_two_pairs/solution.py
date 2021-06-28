class Solution(object):
    def maxProductDifference(self, nums):
        a = nums.pop(nums.index(max(nums)))
        b = nums.pop(nums.index(max(nums)))
        c = nums.pop(nums.index(min(nums)))
        d = nums.pop(nums.index(min(nums)))
        return (a * b) - (c * d)