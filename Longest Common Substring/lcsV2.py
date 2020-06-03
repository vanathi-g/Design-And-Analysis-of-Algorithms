def LCS(s1, s2):
	n = len(s1)
	m = len(s2)
	dp = [[0 for i in range(m)] for i in range(n)]
	for i in range(n):
		for j in range(m):
			if (s1[i] == s2[j]):
				dp[i][j] = dp[i-1][j-1]+1
			else:
				dp[i][j] = max(dp[i-1][j],dp[i][j-1])
	return dp

s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")
dp = LCS(s1, s2)

i = len(s1)-1
j = len(s2)-1
arr = []

#tracing back
while(True):
	ele = dp[i][j]
	if s1[i] == s2[j]:
		arr.append(s1[i])
		i-=1
		j-=1
	elif dp[i-1][j] > dp[i][j-1]:
		i-=1
	else:
		j-=1
	if(i==-1 or j==-1):
		break
print("One of the longest common substrings is:",''.join(arr[::-1]))

'''OUTPUT:
Enter string 1: apqlmnefcr
Enter string 2: mnefaqplcd
One of the longest common substrings is: mnefc
'''
