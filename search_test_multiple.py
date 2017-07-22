

s= 'hello my name'
r = raw_input("enter youur search")
lst = r.split()
n = len(lst)
print n
print(s)
for x in range (0,n):
	print('+' + lst[x])
	#print(lst[x])
