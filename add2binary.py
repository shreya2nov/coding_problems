class Solution(object):
    def addBinary(self, a, b):
        intsum=int(a,2)+int(b,2)
        return (bin(intsum))[2:]
        
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
