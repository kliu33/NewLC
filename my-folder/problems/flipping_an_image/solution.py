class Solution(object):
    def flipAndInvertImage(self, image):
        for i in image:
            i.reverse()
            for j in range(len(i)):
                if i[j] == 0:
                    i[j] = 1
                else: 
                    i[j] = 0
        return image
                
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        