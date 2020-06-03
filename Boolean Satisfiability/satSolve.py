'''PROGRAM DESCRIPTION:
	 Algorithm to solve boolean formula satisfiablility using backtracking
	 Input: text file - first line is number of formulas
	 				followed by the formulas separated by '-'
	 				(see example input.txt for format)
	 Output: Solution that satisfies formula (if it exists)
'''
import math

#Function that formats given input formula
def readFormula(f):
	formula = []
	for ele in f:
		clause = []
		ele = ele.split()
		for var in ele:
			if len(var) == 2: #negate it
				clause.append((var[0], 0))
			else:
				clause.append((var[0], 1))
		formula.append(clause)
	return formula

#Function that displayes the formula as a string
def string(f):
	s = ['[']
	for clause in f:
		s.append('(')
		for var in clause:
			s.append(var[0])
			if var[1] == 0:
				s.append("'")
			s.append('+')
		s[-1] = ')'
	s.append(']')
	s = ''.join(s)
	return s

#Function that returns shortest clause not used during variable listing
def best_clause(f, used):
	minLen = math.inf
	for i in range(len(f)):
		clause = f[i]
		if len(clause) < minLen and i not in used:
			minLen = len(clause)
			clauseNo = i
	return clauseNo

#Generates the list of variables in formula 'f'
def generateVarList(f):
	varList = []
	used = []
	while True:
		num = best_clause(f, used)
		used.append(num)
		for var in f[num]:
			if var[0] not in varList:
				varList.append(var[0])
		if(len(used) == len(f)):
			break
	return varList
	
#Function that simplifies the given formula 'f'
def eval_formula(f, var, val):

	'''Property of OR gates: 1+x = 1 ; 0+x = x
		If a clause evaluates to 1, remove it;
		Otherwise remove only that variable from the clause'''

	g = [] # simplified formula
	for clause in f:
		temp = clause[:]

		for i in range(len(clause)):
			if clause[i][0] == var:
				if clause[i][1] != val:
					temp.pop(i)
					if temp == []:
						temp = ()
				else:
					temp = []
				break

		#If temp = [] it means it evaluated to true, do not include the clause
		if(temp != []): 
			g.append(temp)
	return g

#Core function that solves the given formula 'f'
#Returns None if unsatisfiable, else returns solution
def solve(assign, f):
	global varList
	global level

	#If leaf node in state tree has been reached:
	if level == len(varList):
		level-=1
		return

	#For a variable 'x', two values 0 and 1 can be assigned
	for i in range(0,2):
		var = varList[level]
		assign[var] = i
		level+=1

		#Simplify the formula
		g = eval_formula(f, var, assign[var])
		if g == []: #Solution has been found
			return assign
		ans = solve(assign, g)
		if(ans!=None): #Will not be None only when solution has been found
			return ans

	#Backtrack
	assign.pop(var)
	level-=1
	return ans

#Reading input from text file
print("\n--------------------------------------------------------\n")
fname = input("Enter filename: ")
fp = open(fname, "r")

t = int(fp.readline()) #number of formulas

for case in range(t):
	print("\n--------------------------------------------------------")
	inp = []
	while(True):
		line = fp.readline().strip('\n')
		if(line == '-'):
			break
		inp.append(line)

	#formatting and displaying formula
	f = readFormula(inp)
	print("\nFormula is: "+string(f))

	#setting required global variables
	assignment = {}
	varList = generateVarList(f)
	level = 0

	#solve and print solution (if satisfiable)
	ans = solve(assignment, f)
	print()
	if(ans == None):
		print("No assignment possible")
	else:
		print("Assigned values:")
		for key in ans:
			print(key, "--->", ans[key])

print()
fp.close()