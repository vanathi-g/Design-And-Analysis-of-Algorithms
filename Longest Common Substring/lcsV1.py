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
print("Length of longest common substring is:",dp[len(s1)-1][len(s2)-1])
'''OUTPUT:
Enter string 1: helloworld
Enter string 2: aaworldbye
Length of longest common substring is: 5
'''
