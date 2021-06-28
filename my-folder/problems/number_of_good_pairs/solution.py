class Solution(object):
    def numIdenticalPairs(self, nums):
        pairs = 0
        r = range(len(nums))
        for i in r:
            for j in r:
                if nums[i] == nums[j] and i < j:
                    pairs += 1
        return pairs
        """
        :type nums: List[int]
        :rtype: int
        """
        