class Solution(object):
    def reverse(self, x):
        if x == 0:
            return 0
        elif x > 0:
            revx = int(str(x)[::-1])
        else: 
            revx = -1 * int(str(x)[1:][::-1])
        if abs(revx) > 2**31:
            return 0
        else:
            return revx
        
        """
        :type x: int
        :rtype: int
        """
        