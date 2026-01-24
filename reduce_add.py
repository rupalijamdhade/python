
#using reduce accepts list of numbers and returns addition of all elements
from functools import reduce
nums=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,nums)
print(sum)