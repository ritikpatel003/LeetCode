nums = [1,2,3]
res=[]
def sol(ip,op):
    if ip==[]:
        res.append(op)
    for i in range(len(ip)):
        sol(ip[0:i]+ip[i+1:],op+[ip[i]])
    return res
print(sol(nums,[]))