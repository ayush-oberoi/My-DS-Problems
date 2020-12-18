def mergesortedarray(array1,array2):
	mergedArray = []
	i,j = 0,0
	#check input
	if len(array1) is 0:
		return array2
	if len(array2) is 0:
		return array1

	while i<len(array1) and j<len(array2):
		if array1[i] <= array2[j]:
			mergedArray.append(array1[i])
			i += 1
		elif array2[j] < array1[i]:
			mergedArray.append(array2[j])
			j += 1
	return mergedArray+array1[i:]+array2[j:]

def mergesortarray2(a,b):
	mylist = a+b
	x = sorted(mylist)
	return x
a = [1,3,4,6,20]
b = [2,3,4,5,6,9,11,76]
print("The arrays are",a,b)
print(mergesortedarray(a,b))
print(mergesortarray2(a,b))
