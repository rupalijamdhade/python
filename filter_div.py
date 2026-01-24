num=[12,23,45,34,15,21,20,35,2,1]
div=list(filter(lambda x:x%3==0 and x%5==0,num))
print(div)