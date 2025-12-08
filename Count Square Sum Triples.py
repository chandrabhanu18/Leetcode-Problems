class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                sq=i*i+j*j
                k=int(sq**0.5)
                if k<=n and k*k==sq:
                    c+=1
        return c            
