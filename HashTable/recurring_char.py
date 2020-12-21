def RecurringChar1(MyArray):
	MyHash = {}
	for i in MyArray:
		if MyHash.get(i):
			return i
		else:
			MyHash[i] = 1

print(RecurringChar1([2,5,5,2,3,5,1,2,4]))