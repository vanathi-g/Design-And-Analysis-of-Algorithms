def fast_power(x,n):
	if(n==0):
		return 1
	if(n==1):
		return x
	flag = 0
	if(n%2==1):
		flag=1
	ans=x
	while(n>1):
		ans*=ans
		n//=2
	if(flag==1):
		ans*=x
	return ans

x, n = list(map(int, input("Enter base and power: ").split(' ')))
print("Answer:",fast_power(x,n))

'''OUTPUT:
Enter base and power: 3 0
Answer: 1

Enter base and power: 3 1
Answer: 3

Enter base and power: 3 2
Answer: 9

Enter base and power: 3 3
Answer: 27

Enter base and power: 3 4
Answer: 81

Enter base and power: 3 5 
Answer: 243
'''
