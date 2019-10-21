cnt = 1
i=1
# n = input('Enter number of lines : ')
while(i<5):
	
	if cnt <= i:
		print(i*cnt, end=" ")
		cnt = cnt+1
		continue
	else:
		print(" ")
		i = i+1
		cnt=1
		continue


