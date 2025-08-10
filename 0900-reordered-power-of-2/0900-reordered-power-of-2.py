import itertools as tl
class Solution(object):
    def powerOf2(self,n):
        # i=0
        # while True:
        #     if 2**i==n:
        #         return True
        #     elif 2**i>n:
        #         return False
        #     i+=1
        return n > 0 and (n & (n - 1)) == 0

    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        pt = [''.join(x) for x in tl.permutations(str(n)) if not x[0]=='0']
        bool_lst=[ self.powerOf2(int(x)) for x in pt]
        print(len(bool_lst))
        # return False
        return sum(bool_lst)>0#((sum(bool_lst)/len(bool_lst)) > (len(bool_lst)/2)) #or (len(bool_lst)==1 and (sum(bool_lst)==1)
            

