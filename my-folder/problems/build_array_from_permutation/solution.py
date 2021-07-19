class Solution(object):
    def buildArray(self, nums):
        out = list(nums)
        for i in range(len(nums)):
            out[i] = nums[nums[i]]
        return out
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        