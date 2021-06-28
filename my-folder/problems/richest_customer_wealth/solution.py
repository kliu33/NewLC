class Solution(object):
    def maximumWealth(self, accounts):
        max = 0
        for worth in accounts:
            if sum(worth) > max:
                max = sum(worth)
        return max
                
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        