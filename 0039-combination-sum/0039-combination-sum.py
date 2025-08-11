class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        rr=[]
        
        def checkr(st,r,p):
            if r == 0:
                rr.append(p[:])
                return
            
            for x in range(st,len(candidates)):
                c = candidates[x]
                if c>r:
                    break
                p.append(c)
                checkr(x,r-c,p)
                # checker(x,p,t+candiates[x])
                p.pop()                
        checkr(0,target,[])
        print(rr)
        return rr