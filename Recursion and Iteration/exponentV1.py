def power(x,n):
	if n==1:
		return 1
	return x*power(x,n-1)
x, n = list(map(int, input("Enter base and power: ").split(' ')))
print("Answer:",power(x,n))

'''OUTPUT:
Enter base and power: 3 4
Answer: 27
'''
