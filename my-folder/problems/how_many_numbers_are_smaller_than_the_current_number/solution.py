class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        stack = []
        for i in nums:
            less = 0
            for j in nums:
                if j < i:
                    less += 1
            stack.append(less)
        return stack
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        