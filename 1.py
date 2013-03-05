def AllLessThan(list, value):
	allLessThan = True
	for val in list:
		allLessThan = val < value
		if (not allLessThan):
			break

	return allLessThan

def SomeLessThan(list, value):
	someLessThan = False
	for val in list:
		someLessThan = val < value
		if (someLessThan):
			break

	return someLessThan

some_list1 = [5,3,4,5]
some_list2 = [5,3,7,5]

print AllLessThan(some_list1, 6)
print AllLessThan(some_list2, 6)
print SomeLessThan(some_list1, 6)
print SomeLessThan(some_list2, 6)