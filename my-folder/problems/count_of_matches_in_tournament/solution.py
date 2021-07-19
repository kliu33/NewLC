class Solution(object):
    def numberOfMatches(self, n):
        m = 0
        while n > 1:
            if n % 2 == 1:
                m += n//2
                n = (n//2) + 1
            else: 
                m += n/2
                n /= 2
        return int(m)
        """
        :type n: int
        :rtype: int
        """
        