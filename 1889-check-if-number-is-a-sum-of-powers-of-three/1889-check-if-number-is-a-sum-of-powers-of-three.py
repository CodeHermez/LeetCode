class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        y = n
        for x in range(20,-1,-1):
            if(n-3**x>=0):
                n = n-3**x
        if n==0:
            return True
        else:
            return False