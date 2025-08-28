class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        size=len(grid)
        def getDiag(rev=False,l=0,k=0):
            q = l
            t =k
            diag = []
            while q<size and t<size:
                diag.append(grid[q][t])
                q+=1
                t+=1
            
            diag.sort(reverse=rev)
            q = l
            t =k

            for x in diag:
                grid[q][t]=x
                q+=1
                t+=1

        for r in range(size):
            getDiag(True,l=r)

        for c in range(1,size):
            getDiag(k=c,l=0)
            
        return grid
                