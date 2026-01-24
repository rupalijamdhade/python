from functools import reduce
nums=[1,2,34,2,4,33,45]
maximum=reduce(lambda x,y:x if x<y else y,nums)
print(maximum)
