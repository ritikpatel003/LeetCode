class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n=len(nums)
        w=sum(nums)-S
        if w<0:
            return 0
        dp=[[0 for i in range(w+1)] for i in range(n+1)]
        dp[0][0]=1
        p=0
        for i in range(1,n+1):
            if nums[i-1]==0:
                p+=1
            dp[i][0]=2**p
        for i in range(1,n+1):
            for j in range(1,w+1):
                if j-2*nums[i-1]>=0:
                    dp[i][j]=dp[i-1][j-2*nums[i-1]]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return (dp[-1][-1])