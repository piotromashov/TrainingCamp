from binarySearch import binarySearchUpper

# Description

# Students from UPRM are holding a fundraising game in which people donate money to participate. When the total amount donated matches or surpasses a certain goal, the person who made the donation receives a prize. Given a series of donations in the order in which they arrived and a reward goal, determine which donor will receive the prize.
# Input specification

# The input will begin with a line containing an integer N (1 <= N <= 105) denoting the number of donations. The following N lines will each contain an integer A (1 <= A <= 100) denoting an amount of dollars that was donated. Then a single line with an integer Q (1 <= Q <= 105) will follow, denoting the number of queries. The next Q lines will each contain an integer R (1 <= R <= 107) indicating the reward goal for which you must find the winner (in dollars).
# Output specification

# For each query, output a single line with an integer indicating the number of the donor who won the donation prize. That will be the donor who made the first donation that pushed the total amount of donations up to or past the reward goal. If no such donor exists, then the output must be "none". The order of the results must follow the same order in which the queries are provided.

total_doners = int(raw_input())
doners = []
donationsAcumulated = 0
for _ in xrange(0, total_doners):
	doner = int(raw_input())
	donationsAcumulated += doner
	doners.append(donationsAcumulated)
	
total_queries = int(raw_input())
for _ in xrange(0,total_queries):
	query = int(raw_input())
	first = 0
	last = total_doners-1
	found = False
	result = -1
	while first <= last and not found:
		midpoint = (first+last)//2
		if doners[midpoint] >= query and (midpoint == 0 or doners[midpoint-1] < query):
			found = True
			result = midpoint
		else:
			if query < doners[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1
	if result >= 0:
		print result+1 
	else:
		print "none"

f = open("supertest.txt", "w")
f.write("100000\n")
for i in xrange(0,100000):
	f.write("100")
	f.write("\n")
f.write("100000\n")
for i in xrange(0,100000):
	if i % 2 == 0:
		f.write("9999999\n")
	else:
		f.write("1\n")
f.close()