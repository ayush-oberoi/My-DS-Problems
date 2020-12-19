#Find duplicates of an array without set with hash table
#o(n)

def FindDuplicate(MyArray):
  l = []
  MyDictionary = dict()
  for i in MyArray:
    if i not in MyDictionary:
      MyDictionary[i] = 0
      l.append(str(i))
    else:
      MyDictionary[i] += 1
      
  return ' '.join(l)

#Find duplicates of an array without set without hash table
def FindDuplicate1(MyArray):
  return (' '.join([str(n) for i,n in enumerate(MyArray) if n not in MyArray[:i]]))

l = FindDuplicate([1,2,3,4,4,2,5,6,5,6])
li = FindDuplicate1([1,2,3,4,4,2,5,6,5,6])
print(l)
print(li)