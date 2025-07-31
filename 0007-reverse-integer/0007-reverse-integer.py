class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        a = 120
        val = 0
        if(x<0):
            x*=-1
            val = int(str(x)[::-1])
            val*=-1
        else:
            val =int(str(x)[::-1])

        if(val.bit_length()>=32):
            return 0

        return val
    