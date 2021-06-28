class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            for i in nums:
                if i > target:
                    return nums.index(i)
            return len(nums)
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        