class Solution(object):
    def hammingWeight(self, n):
        out = [0] * 32
        for i in range(32):
            if n != 0:
                if n % 2 == 1:
                    out[-(i+1)] = 1
                n //= 2
        return out.count(1)
        """
        :type n: int
        :rtype: int
        """
        