class Solution(object):
    def plusOne(self, digits):
        mid = 0
        for i in range(len(digits)):
            mid = (mid * 10) + digits.pop(0)
        mid += 1
        while mid > 0:
            digits.append(mid % 10)
            mid = (mid - (mid % 10)) / 10
        digits.reverse()
        return digits
            
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        