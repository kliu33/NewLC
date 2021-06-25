class Solution(object):
    def shuffle(self, nums, n):
        x = []
        r = []
        for i in range(n):
            x.append(nums[0])
            nums.pop(0)
        for i in range(n):
            r.append(x[i])
            r.append(nums[i])
        return r
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        