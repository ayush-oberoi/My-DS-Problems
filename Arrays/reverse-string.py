def reverse(myarray):
	l = []
	for i in range(len(myarray)-1,-1,-1):
		l.append(myarray[i])
	return ''.join(l)
def reverse1(array):
	return array[::-1]
print(reverse("Azure Cloud is Awesome"))
print(reverse1("Google Cloud is Awesome"))
