n = 4
arr = [[1,2,3,5],[4,5,6,7],[7,8,9,8],[2,3,4,7]]
l =[]

print(arr)

for i in range(n):
	m=i
	j=0
	s=0
	while(j<=i and m>=0):
		s += arr[m][j]
		
		if m==0:
			break
		else:
			m=m-1
		j=j+1

	print(s)

	l.append(s)
	continue;

i = n-1
for j in range(1,n):
	m = i
	p = j

	s=0
	while(p<=i):
		s += arr[m][p]

		m = m-1
		p = p+1

	print(s)
	l.append(s)
	continue


