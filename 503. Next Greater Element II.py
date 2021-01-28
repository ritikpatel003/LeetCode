class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if nums==[]:
            return []
        x=len(nums)
        nums+=nums
        st=[nums[-1]]
        a=[-1]
        for i in nums[0:-1][::-1]:
            if st[-1]<=i:
                while(st[-1]<=i):
                    st.pop()
                    if st==[]:
                        break
                if st==[]:
                    a.append(-1)
                    st.append(i)
                else:
                    a.append(st[-1])
                    st.append(i)
            else:
                a.append(st[-1])
                st.append(i)
        return(a[::-1][0:x])