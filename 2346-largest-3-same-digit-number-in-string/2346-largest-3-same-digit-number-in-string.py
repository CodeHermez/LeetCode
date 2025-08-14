class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        list = []
        for x in range(len(num)-2):
            if num[x:x+3][0]==num[x:x+3][1] and num[x:x+3][1] ==num[x:x+3][2]:
                    list.append(num[x:x+3])
        
        if not len(list)==0:
            return max(list)
        else:
            return ''
     