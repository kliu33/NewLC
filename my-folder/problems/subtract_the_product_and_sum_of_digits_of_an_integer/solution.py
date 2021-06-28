class Solution(object):
    def subtractProductAndSum(self, n):
        prod = 1
        su = 0
        arr = []
        while n > 0:
            arr.append(n % 10)
            n = (n - (n % 10)) / 10
        arr.reverse()
        for i in arr:
            prod *= i
            su += i
        return prod-su
        """
        :type n: int
        :rtype: int
        """
        