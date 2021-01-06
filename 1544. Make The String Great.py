s = "leEeetcode"
if len(s)<2:
	print(s)
s=list(s)
def sol(s,st):
	if len(st)>1 and abs(ord(st[-1])-ord(st[-2]))==32:
		st.pop()
		st.pop()
	if s==[]:
		return st
	st+=s[0]
	sol(s[1::],st)
	return st
print(sol(s,[]))

