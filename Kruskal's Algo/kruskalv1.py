class unionFind:
        def __init__(self, n):
                self.parent = [-1 for i in range(0,n+1)]
        def Insert(self, u, v):
                if self.parent[u] == -1:
                        self.parent[v] = u
                else:
                        self.parent[v] = self.parent[u]

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


print("--------UNION FIND DEMO---------\n")
m = int(input("Enter total number of vertices: "))
V = unionFind(m)

print("--Enter two disjoint subgraphs--\n")
n1 = int(input("Number of edges in SG1: "))
subG1 = []
for i in range(n1):
        u, v = map(int, input().split(' '))
        subG1.append((u,v))
        V.Insert(u,v)

n2 = int(input("Number of edges in SG2: "))
subG2 = []
for i in range(n2):
        u, v = map(int, input().split(' '))
        subG2.append((u,v))
        V.Insert(u,v)

print("\n----------DEMO OF FIND----------\n");
v1, v2 = map(int, input("Enter two no.s to find their root: ").split(' '))
r1 = V.Find(v1)
r2 = V.Find(v2)
print("Roots of",v1,"and",v2,"are:",r1,"and",r2);

print("\n----------DEMO OF UNION---------\n");
print("Parent array before union: ",V.parent)
V.Union(r1, r2)
print("Parent array after union: ",V.parent)

'''OUTPUT:

--------UNION FIND DEMO---------

Enter total number of vertices: 5
--Enter two disjoint subgraphs--

Number of edges in SG1: 2
1 2
2 3
Number of edges in SG2: 1
4 5

----------DEMO OF FIND----------

Enter two no.s to find their root: 3 5
Roots of 3 and 5 are: 1 and 4

----------DEMO OF UNION---------

Parent array before union:  [-1, -1, 1, 1, -1, 4]
Parent array after union:  [-1, 4, 1, 1, -1, 4]

'''
