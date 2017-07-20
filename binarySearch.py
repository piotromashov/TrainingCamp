#returns index of found upper bound 
def binarySearchUpper(alist, item):
	first = 0
	last = len(alist)-1
	found = False
	while first <= last and not found:
		midpoint = (first+last)//2
		if alist[midpoint] >= item and (midpoint == 0 or alist[midpoint-1] < item):
			found = True
			return midpoint
		else:
			if item < alist[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1
	return -1
