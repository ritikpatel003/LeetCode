graph = [[1,2],[3],[3],[]]
res=[]
def sol(a,b):
    if a==len(graph)-1:
        res.append(b+[a])
        return b
    for i in graph[a]:
        sol(i,b+[a])
    return res
print(sol(0,[]))