class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        trap =num
        string = ''
        r = 0
        w = 0
        if num==0:
            return str(num)
        elif(trap>0):
            while(trap>0):
                r = trap%7
                trap = trap//7
                string = str(r) + string
        else:
            trap*=-1
            while(trap!=0):
                print(trap)
                r = trap%7
                trap = trap//7
                string = str(r) + string
            string = '-'+string
        print('\n\n',string)
        return string
            
            