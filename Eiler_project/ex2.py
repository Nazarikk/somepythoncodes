c=0
a=1
b=0
sum=0
while(a<4000000):
	c=b
	b=a
	a+=c
	if(a%2==0):
		sum+=a
print(sum)
