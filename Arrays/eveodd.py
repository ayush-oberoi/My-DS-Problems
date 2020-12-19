#Program to arrange a given array with first even element
#then odd elements in o(n)
n = int(input())
MyArray = list(map(int,input().split()))
EvenArray , OddArray = list() , list()
for i in MyArray:
  if i%2 == 0:
    EvenArray.append(str(i))
  else:
    OddArray.append(str(i))
print(' '.join(EvenArray+OddArray))