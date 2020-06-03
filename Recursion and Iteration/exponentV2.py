def power(x,n):
	prod = 1
	for i in range(1,n):
		prod*=x
	return prod

x, n = list(map(int, input("Enter base and power: ").split(' ')))
print("Answer:",power(x,n))

'''OUTPUT:
Enter base and power: 3 4 
Answer: 27
'''
