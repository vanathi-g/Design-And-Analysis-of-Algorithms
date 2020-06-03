def fast_power(x,n):
	if n==0:
		return 1
	if n%2==0:
		return x*fast_power(x,n-1)
	else:
		return x*fast_power(x,n//2)*fast_power(x,n//2)
		
x, n = list(map(int, input("Enter base and power: ").split(' ')))
print("Answer:",fast_power(x,n-1))

'''OUTPUT:
Enter base and power: 3 4
Answer: 27
Enter base and power: 3 5
Answer: 81
'''
