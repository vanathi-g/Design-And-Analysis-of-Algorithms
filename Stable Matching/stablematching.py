'''
Program to solve stable matching problem - Gale Shapeley Algorithm
#INPUT: input.txt (single space separated names of men/women)
SAMPLE INPUT USED:
a u r t s
b r t u s
c t u s r
d u r t s

r a c d b
s d a b c
t c b d a
u b d c a
'''

''' FUNCTION DEFINITIONS '''
def propose(m):
	#iterating through women from most to least preferred
	for w in menPref[m]:
		#if most preferred woman is unmatched:
		if w not in matches:
			accept(m, w)
			global unmatched
			unmatched-=1
			return
		#check whether the most preferred woman is in an unstable match
		if isUnstable(m, w):
			reject(w)
			accept(m, w)
			return
	return

def accept(m,w):
	matches[w] = m
	return

def reject(w):
	del matches[w]
	return

def isUnstable(m,w):
	#remember, men are arranged in descending order of preference
	if womenPref[w].index(m) < womenPref[w].index(matches[w]):
		return True
	return False

def sortKey(val):
	return val[1]

#first read input from text file names "input.txt"
flag = 0
file = open("input.txt")
menPref = dict()
womenPref = dict()
for line in file:
	if line=="\n":
		flag = 1
		continue
	temp = line.split()
	if flag == 0:
		menPref[temp[0]] = temp[1:]
	else:
		womenPref[temp[0]] = temp[1:]
file.close()

#menPref is a dictionary containing each man's preferences, indexed by the man's name
#similarly womenPref contains women's preferences

#we can keep a global dictionary that keeps track of current matches, indexed by women's names
matches = dict()
unmatched = len(womenPref)

#while there is an unmatched man/woman, make the men propose
while(unmatched > 0):
	for man in menPref:
		if man not in matches.values(): #if man is unmatched
			propose(man)

stableMatch = list(matches.items())	
stableMatch.sort(key=sortKey)
print("Man <---> Woman")
for match in stableMatch:
	print(match[1],"  <--->",match[0])

'''OUTPUT:
Man <---> Woman
a   <---> r
b   <---> u
c   <---> t
d   <---> s

'''
