def match(nuts, bolts):
	for nut in nuts:
		for bolt in bolts:
			if nut == bolt:
				print(nut, "matched with", bolt)

nuts = list(map(int, input("Enter nuts: ").split(' ')))
bolts = list(map(int, input("Enter bolts: ").split(' ')))
match(nuts, bolts)

'''OUTPUT:
Enter nuts: 2 1 7 4 5 6
Enter bolts: 6 5 1 4 7 2
2 matched with 2
1 matched with 1
7 matched with 7
4 matched with 4
5 matched with 5
6 matched with 6
'''
