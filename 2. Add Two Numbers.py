class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a1=[]
        while(l1!=None):
            a1.append(l1.val)
            l1=l1.next
        a2=[]
        while(l2!=None):
            a2.append(l2.val)
            l2=l2.next
        s1=""
        s2=""
        for i in a1[::-1]:
            s1+=str(i)
        for i in a2[::-1]:
            s2+=str(i)
        res=int(s1)+int(s2)
        ans=[]
        for i in str(res)[::-1]:
            ans.append(int(i))
        x=ListNode(0)
        r=x
        for i in ans[0:-1]:
            x.val=i
            y=ListNode(0)
            x.next=y
            x=x.next
        x.val=ans[-1]
        return r
