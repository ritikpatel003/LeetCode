class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        res=[]
        pos=[]
        X=[x]
        Y=[y]
        d={}
        def sol(x,k):
            if x!=None:
                if x.val==X[0]:
                    d[X[0]]=k
                if x.val==Y[0]:
                    d[Y[0]]=k
                sol(x.left,k+1)
                sol(x.right,k+1)
                if x.left!=None:
                    if x.left.val==X[0]:
                        X.append(x.val)
                    if x.left.val==Y[0]:
                        Y.append(x.val)
                if x.right!=None:
                    if x.right.val==X[0]:
                        X.append(x.val)
                    if x.right.val==Y[0]:
                        Y.append(x.val)
            return 0
        sol(root,0)
        print(d[x])
        if d[x]==d[y] and X[1]!=Y[1]:
            return True
        else:
            return False