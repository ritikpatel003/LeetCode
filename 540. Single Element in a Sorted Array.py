class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[-1]!=nums[-2]:
            return nums[-1]
        l=1
        r=len(nums)-2
        while(r>=l):
            m=(l+r)//2
            if nums[m]!=nums[m-1] and nums[m]!=nums[m+1]:
                break
            elif nums[m-1]==nums[m] and m%2==0:
                r=m-1
            elif nums[m]==nums[m+1] and m%2==1:
                r=m-1
            else:
                l=m+1
        return nums[m]