A = []
B = []
C = []
b='1346'
c='+-*/'
v=' -  '
o=0
p=0
global su
su = 0

def tiv(n,b):
	w = ''
	for i in b:
		if i != n:
			w +=i
	return w


for i in b:
	for j in tiv(i,b):
		for k in tiv(j,tiv(i,b)):
			for l in tiv(k,tiv(j,tiv(i,b))):
				# for t in v:
				for f in c:
					for g in c:
						for h in c:
							B.append((int(i),f,int(j),g,int(k),h,int(l)))
							B.append((int(i),f,"(",int(j),g,int(k),h,int(l),")"))
							B.append((int(i),f,"(",int(j),g,"(",int(k),h,int(l),")",")"))
							B.append((int(i),f,"(","(",int(j),g,int(k),")",h,int(l),")"))
							B.append((int(i),f,int(j),g,"(",int(k),h,int(l),")"))
							p+=5
				o+=1
				C.append((int(i),int(j),int(k),int(l)))


with open('test.txt', 'wt', encoding='utf-8') as inFile:
	z=0
	for i in B:
		B[z]=''.join(str(x) for x in i)
		inFile.write(B[z])
		inFile.write("\n")
		z+=1

for i in B:
	print(i,"\n")

print("tveri hamadr = ",o," gorcoxuty hamadr = ",p)

