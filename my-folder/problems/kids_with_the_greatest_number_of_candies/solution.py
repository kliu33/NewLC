class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        m = max(candies)
        stack = []
        for candy in candies:
            if candy + extraCandies >= m:
                stack.append(True)
            else:
                stack.append(False)
        return stack
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        