#using filter()accepts list of numbers and return list of even number
nums=[1,22,33,4,2,21,52,12,8,4,6]
even_nums=list(filter(lambda x:x%2==0,nums))
print(even_nums)