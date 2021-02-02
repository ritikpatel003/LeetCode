class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        a=0
        def task(a,N,K):
            global ans,k
            if N==0:
                ans = a
                k = K
                return
            if K>(2**(N-1))//2:
                K-=(2**(N-1))//2
                N-=1
                a+=1
                task(a,N,K)
            else:
                N-=1
                task(a,N,K)
        task(a,N,K)
        if ans%2==0:
            return(1)
        else:
            return(0)