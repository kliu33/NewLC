class Solution(object):
    def romanToInt(self, s):
        total = 0
        total = s.count("I")
        total += s.count("V") * 5
        total += s.count("X") * 10
        total += s.count("L") * 50
        total += s.count("C") * 100
        total += s.count("D") * 500
        total += s.count("M") * 1000
        total -= s.count("IV") * 2
        total -= s.count("IX") * 2
        total -= s.count("XL") * 20
        total -= s.count("XC") * 20
        total -= s.count("CD") * 200
        total -= s.count("CM") * 200
        return total
        """
        :type s: str
        :rtype: int
        """
        