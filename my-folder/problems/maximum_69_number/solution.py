class Solution(object):
    def maximum69Number (self, num):
        s = str(num)
        s = s.replace("6","9",1)
        return int(s)
        """
        :type num: int
        :rtype: int
        """
        