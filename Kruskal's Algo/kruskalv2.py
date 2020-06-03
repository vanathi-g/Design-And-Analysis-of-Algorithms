class unionFind:
	def __init__(self, n):
		self.parent = [-1 for i in range(0,n+1)]
	
	def Insert(self, u, v):
		self.parent[v] = u
		
	def Find(self,e): #return root of subset of e
		while True:
			if self.parent[e] == -1:
				break
			e = self.parent[e]
		return e
				
	def Union(self, b1,b2):
		if self.parent[b1] == -1:
		    self.parent[b1] = b2
		else:
		    self.parent[b1] = self.parent[b2]

def Kruskal(E, V):
	S = unionFind(m)
	T = []
	tempE = sorted(E, key=lambda x:x[2])
	for edge in tempE:
		u = edge[0]
		v = edge[1]
		#print(u, S.Find(u), v, S.Find(v))
		if S.Find(u) != S.Find(v):
			S.Union(u,v)
			T.append(edge)
		#print(S.parent)
	return T

m = int(input("Enter number of vertices: "))
n = int(input("Enter number of edge-cost pairs: "))
arr=[]
print("Enter the edge cost pairs as 'u v cost': ")
for i in range(n):
	u, v, e = map(int, input().split(' '))
	arr.append((u,v,e))
MST = Kruskal(arr,m)
print("\n---------------------------\n")
totCost=0
for i in range(0,len(MST)):
    print("Edge",i+1,"is",MST[i][0],"->",MST[i][1],"& cost =",MST[i][2])
    totCost+=MST[i][2]
print("\nTotal cost of MST=",totCost);


'''OUTPUT:
Enter number of vertices: 5
Enter number of edge-cost pairs: 7
Enter the edge cost pairs as 'u v cost': 
1 3 1
1 5 2
1 4 3
1 2 4
2 4 1
4 5 2
5 3 3

---------------------------

Edge 1 is 1 -> 3 & cost = 1
Edge 2 is 2 -> 4 & cost = 1
Edge 3 is 1 -> 5 & cost = 2
Edge 4 is 4 -> 5 & cost = 2
Edge 5 is 1 -> 4 & cost = 3
Edge 6 is 5 -> 3 & cost = 3

Total cost of MST= 12
'''
