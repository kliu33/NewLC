class Solution(object):
    def minOperations(self, boxes): #boxes = 110
        arr = []
        fin = []
        for i in boxes:
            arr.append(i)  #arr = [1, 1, 0]
        for check in range(len(arr)):
            moves = 0
            for i in range(len(arr)):
                if i != check and arr[i] == "1":
                    moves += abs(check - i)
            fin.append(moves)
        return fin
            
            
        """
        :type boxes: str
        :rtype: List[int]
        """
        