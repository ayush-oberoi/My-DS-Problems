def reverse(myarray):
	l = []
	for i in range(len(myarray)-1,-1,-1):
		l.append(myarray[i])
	return ''.join(l)
print(reverse("Azure Cloud is Awesome"))
