#using filter()accepts list of numbers and return list of odd number
nums=[1,25,33,4,2,21,52,121,8,4,61]
odd_nums=list(filter(lambda x:x%2==1,nums))
print(odd_nums)