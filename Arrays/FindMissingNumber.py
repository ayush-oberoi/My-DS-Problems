#Program to find a missing number from a list of 1 to 100
#in o(n)
def FindMissingNumber(NumArr):
  numlength = len(NumArr)
  n = NumArr[numlength-1]
  NumSum = (n* (n+1)) // 2
  Arraysum = sum(NumArr)
  return NumSum - Arraysum
l = list(range(1,50)) + list(range(51,101))
print(FindMissingNumber(l))
